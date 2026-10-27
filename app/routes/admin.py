from datetime import date
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import db, User, Book, Loan, LibrarySettings
from app.forms import BookForm, SettingsForm
from app.decorators import admin_required

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
@admin_required
def dashboard():
    """Admin dashboard with high-level analytics, active loans, and overdue counts."""
    settings = LibrarySettings.get_settings()
    
    total_users = User.query.filter_by(role='student').count()
    total_books = Book.query.count()
    total_copies = db.session.query(db.func.sum(Book.total_copies)).scalar() or 0
    total_available_copies = db.session.query(db.func.sum(Book.available_copies)).scalar() or 0
    
    active_loans = Loan.query.filter_by(status='issued').all()
    active_loans_count = len(active_loans)
    
    # Calculate overdue loans and total outstanding fines across the entire system
    overdue_loans_count = 0
    total_outstanding_fines = 0.0

    for loan in active_loans:
        fine = loan.calculate_current_fine(daily_rate=settings.daily_fine_rate)
        total_outstanding_fines += fine
        if loan.is_overdue:
            overdue_loans_count += 1

    # Include unpaid returned loans
    unpaid_loans = Loan.query.filter_by(status='returned', fine_paid=False).all()
    for loan in unpaid_loans:
        total_outstanding_fines += loan.calculated_fine

    # Recent transactions
    recent_loans = Loan.query.order_by(Loan.created_at.desc()).limit(6).all()

    # Most borrowed books
    most_borrowed = (
        db.session.query(Book, db.func.count(Loan.id).label('loan_count'))
        .join(Loan, Book.id == Loan.book_id)
        .group_by(Book.id)
        .order_by(db.desc('loan_count'))
        .limit(5)
        .all()
    )

    return render_template('admin/dashboard.html',
                           total_users=total_users,
                           total_books=total_books,
                           total_copies=total_copies,
                           total_available_copies=total_available_copies,
                           active_loans_count=active_loans_count,
                           overdue_loans_count=overdue_loans_count,
                           total_outstanding_fines=round(total_outstanding_fines, 2),
                           recent_loans=recent_loans,
                           most_borrowed=most_borrowed,
                           settings=settings)


@admin_bp.route('/books')
@admin_required
def manage_books():
    """Admin view for managing books catalogue with search and pagination."""
    query = request.args.get('q', '').strip()
    category = request.args.get('category', '').strip()
    page = request.args.get('page', 1, type=int)

    books_query = Book.query

    if query:
        pattern = f"%{query}%"
        books_query = books_query.filter(
            (Book.title.ilike(pattern)) |
            (Book.author.ilike(pattern)) |
            (Book.isbn.ilike(pattern))
        )
    if category:
        books_query = books_query.filter(Book.category == category)

    pagination = books_query.order_by(Book.created_at.desc()).paginate(page=page, per_page=10, error_out=False)
    books = pagination.items
    categories = [c[0] for c in Book.query.with_entities(Book.category).distinct().order_by(Book.category).all()]

    return render_template('admin/books.html', books=books, pagination=pagination, query=query, category=category, categories=categories)


@admin_bp.route('/books/add', methods=['GET', 'POST'])
@admin_required
def add_book():
    """Allows admin to add a new book to the catalogue."""
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(
            title=form.title.data.strip(),
            author=form.author.data.strip(),
            isbn=form.isbn.data.strip(),
            category=form.category.data.strip(),
            publication_year=form.publication_year.data,
            total_copies=form.total_copies.data,
            available_copies=form.total_copies.data,  # Initially all copies are available
            description=form.description.data.strip() if form.description.data else None
        )
        db.session.add(new_book)
        db.session.commit()
        flash(f'Book "{new_book.title}" added successfully!', 'success')
        return redirect(url_for('admin.manage_books'))

    return render_template('admin/book_form.html', form=form, title="Add New Book")


@admin_bp.route('/books/edit/<int:book_id>', methods=['GET', 'POST'])
@admin_required
def edit_book(book_id):
    """Allows admin to edit an existing book's details."""
    book = Book.query.get_or_404(book_id)
    form = BookForm(original_isbn=book.isbn, obj=book)

    if form.validate_on_submit():
        # Prevent reducing total copies below currently borrowed copies
        borrowed_copies = book.total_copies - book.available_copies
        if form.total_copies.data < borrowed_copies:
            flash(f'Cannot reduce total copies below {borrowed_copies} because {borrowed_copies} copies are currently issued to students.', 'danger')
            return render_template('admin/book_form.html', form=form, title=f"Edit {book.title}")

        # Update available copies relative to total copies difference
        diff = form.total_copies.data - book.total_copies
        book.available_copies += diff
        book.total_copies = form.total_copies.data
        book.title = form.title.data.strip()
        book.author = form.author.data.strip()
        book.isbn = form.isbn.data.strip()
        book.category = form.category.data.strip()
        book.publication_year = form.publication_year.data
        book.description = form.description.data.strip() if form.description.data else None

        db.session.commit()
        flash(f'Book "{book.title}" updated successfully!', 'success')
        return redirect(url_for('admin.manage_books'))

    return render_template('admin/book_form.html', form=form, title=f"Edit {book.title}")


@admin_bp.route('/books/delete/<int:book_id>', methods=['POST'])
@admin_required
def delete_book(book_id):
    """Safely deletes a book only if it has no active loans."""
    book = Book.query.get_or_404(book_id)

    if book.has_active_loans():
        flash(f'Cannot delete "{book.title}": There are active loan records for this book.', 'danger')
        return redirect(url_for('admin.manage_books'))

    try:
        # Note: Past returned loans can be unlinked or retained as historical reference
        db.session.delete(book)
        db.session.commit()
        flash(f'Book "{book.title}" was deleted from catalogue.', 'info')
    except Exception as e:
        db.session.rollback()
        flash(f'Unable to delete book: It has borrowing history attached.', 'danger')

    return redirect(url_for('admin.manage_books'))


@admin_bp.route('/loans')
@admin_required
def manage_loans():
    """Admin view for all borrowing transactions with filters and actions."""
    status_filter = request.args.get('status', 'all')
    page = request.args.get('page', 1, type=int)

    query = Loan.query

    if status_filter == 'active':
        query = query.filter_by(status='issued')
    elif status_filter == 'returned':
        query = query.filter_by(status='returned')
    elif status_filter == 'overdue':
        today = date.today()
        query = query.filter(
            ((Loan.status == 'issued') & (Loan.due_date < today)) |
            ((Loan.status == 'returned') & (Loan.return_date > Loan.due_date))
        )

    pagination = query.order_by(Loan.created_at.desc()).paginate(page=page, per_page=10, error_out=False)
    loans = pagination.items
    settings = LibrarySettings.get_settings()

    return render_template('admin/loans.html',
                           loans=loans,
                           pagination=pagination,
                           status_filter=status_filter,
                           daily_fine_rate=settings.daily_fine_rate)


@admin_bp.route('/loans/return/<int:loan_id>', methods=['POST'])
@admin_required
def process_admin_return(loan_id):
    """Admin override to mark a book returned."""
    loan = Loan.query.get_or_404(loan_id)
    settings = LibrarySettings.get_settings()

    if loan.status == 'returned':
        flash('This loan is already closed.', 'info')
        return redirect(url_for('admin.manage_loans'))

    loan.return_date = date.today()
    loan.status = 'returned'
    fine = loan.calculate_current_fine(daily_rate=settings.daily_fine_rate)
    loan.calculated_fine = fine
    if fine == 0:
        loan.fine_paid = True
    loan.book.available_copies += 1

    db.session.commit()
    flash(f'Return processed for "{loan.book.title}". Fine calculated: ₹{fine:.2f}.', 'success')
    return redirect(url_for('admin.manage_loans'))


@admin_bp.route('/loans/pay-fine/<int:loan_id>', methods=['POST'])
@admin_required
def mark_fine_paid(loan_id):
    """Records payment for an outstanding fine."""
    loan = Loan.query.get_or_404(loan_id)
    if loan.fine_paid:
        flash('Fine is already marked as paid.', 'info')
    else:
        loan.fine_paid = True
        db.session.commit()
        flash(f'Payment of ₹{loan.calculated_fine:.2f} recorded successfully for {loan.user.name}.', 'success')

    return redirect(url_for('admin.manage_loans'))


@admin_bp.route('/users')
@admin_required
def manage_users():
    """Lists registered students and their active borrowing statistics."""
    users = User.query.filter_by(role='student').order_by(User.created_at.desc()).all()
    return render_template('admin/users.html', users=users)


@admin_bp.route('/settings', methods=['GET', 'POST'])
@admin_required
def settings():
    """Allows admin to configure borrowing duration, fines, and borrowing limits."""
    current_settings = LibrarySettings.get_settings()
    form = SettingsForm(obj=current_settings)

    if form.validate_on_submit():
        current_settings.borrow_duration_days = form.borrow_duration_days.data
        current_settings.daily_fine_rate = form.daily_fine_rate.data
        current_settings.max_borrow_limit = form.max_borrow_limit.data
        db.session.commit()
        flash('Library settings successfully updated!', 'success')
        return redirect(url_for('admin.settings'))

    return render_template('admin/settings.html', form=form)
