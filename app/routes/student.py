from datetime import date, timedelta
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import db, Book, Loan, LibrarySettings

student_bp = Blueprint('student', __name__, url_prefix='/student')

@student_bp.route('/dashboard')
@login_required
def dashboard():
    """Student dashboard displaying key metrics and recent loan transactions."""
    settings = LibrarySettings.get_settings()
    
    # User's loan stats
    user_loans = Loan.query.filter_by(user_id=current_user.id)
    active_loans = user_loans.filter_by(status='issued').all()
    returned_loans_count = user_loans.filter_by(status='returned').count()
    
    # Calculate overdue loans and live outstanding fine
    overdue_count = 0
    total_outstanding_fine = 0.0

    for loan in active_loans:
        fine = loan.calculate_current_fine(daily_rate=settings.daily_fine_rate)
        total_outstanding_fine += fine
        if loan.is_overdue:
            overdue_count += 1

    # Include unpaid fines from past returned loans
    unpaid_returned_loans = user_loans.filter_by(status='returned', fine_paid=False).all()
    for loan in unpaid_returned_loans:
        total_outstanding_fine += loan.calculated_fine

    # Total books available in the entire library
    total_books_available = db.session.query(db.func.sum(Book.available_copies)).scalar() or 0

    # Recent activity
    recent_loans = user_loans.order_by(Loan.created_at.desc()).limit(5).all()

    return render_template('student/dashboard.html',
                           total_books_available=total_books_available,
                           active_loans_count=len(active_loans),
                           returned_loans_count=returned_loans_count,
                           overdue_count=overdue_count,
                           total_outstanding_fine=round(total_outstanding_fine, 2),
                           active_loans=active_loans,
                           recent_loans=recent_loans,
                           settings=settings)


@student_bp.route('/issue/<int:book_id>', methods=['POST'])
@login_required
def issue_book(book_id):
    """Issues an available book to the current student."""
    book = Book.query.get_or_404(book_id)
    settings = LibrarySettings.get_settings()

    # Rule 1: Check if user already reached maximum borrow limit
    active_count = current_user.get_active_loans_count()
    if active_count >= settings.max_borrow_limit:
        flash(f'Cannot issue book: You have reached the maximum borrow limit of {settings.max_borrow_limit} books.', 'danger')
        return redirect(url_for('main.book_detail', book_id=book.id))

    # Rule 2: Check if user already has an active loan of this exact book
    existing_loan = Loan.query.filter_by(user_id=current_user.id, book_id=book.id, status='issued').first()
    if existing_loan:
        flash('You already have an active borrowed copy of this book.', 'warning')
        return redirect(url_for('main.book_detail', book_id=book.id))

    # Rule 3: Check stock availability
    if book.available_copies <= 0:
        flash('Sorry, this book is currently out of stock.', 'danger')
        return redirect(url_for('main.book_detail', book_id=book.id))

    # Transaction: Safely decrement stock and create loan record
    try:
        book.available_copies -= 1
        
        issue_d = date.today()
        due_d = issue_d + timedelta(days=settings.borrow_duration_days)

        new_loan = Loan(
            user_id=current_user.id,
            book_id=book.id,
            issue_date=issue_d,
            due_date=due_d,
            status='issued'
        )

        db.session.add(new_loan)
        db.session.commit()
        flash(f'Successfully issued "{book.title}"! Due date is {due_d.strftime("%d %b %Y")}.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error issuing book: {str(e)}', 'danger')

    return redirect(url_for('student.dashboard'))


@student_bp.route('/return/<int:loan_id>', methods=['POST'])
@login_required
def return_book(loan_id):
    """Allows student to return a book they borrowed."""
    loan = Loan.query.get_or_404(loan_id)
    settings = LibrarySettings.get_settings()

    # Ownership check: Students can only return their own loans
    if loan.user_id != current_user.id and not current_user.is_admin:
        flash('Unauthorized: You cannot return a loan belonging to another user.', 'danger')
        return redirect(url_for('student.dashboard'))

    # Check if already returned
    if loan.status == 'returned':
        flash('This book has already been marked as returned.', 'info')
        return redirect(url_for('student.dashboard'))

    # Safe return transaction
    try:
        actual_return_date = date.today()
        loan.return_date = actual_return_date
        loan.status = 'returned'
        
        # Calculate final fine
        fine_due = loan.calculate_current_fine(daily_rate=settings.daily_fine_rate)
        loan.calculated_fine = fine_due
        if fine_due == 0:
            loan.fine_paid = True  # Automatically paid if 0
            
        # Increment available copies by exactly 1
        loan.book.available_copies += 1

        db.session.commit()
        
        if fine_due > 0:
            flash(f'Book returned successfully. Late fine due: ₹{fine_due:.2f} ({loan.overdue_days} days overdue).', 'warning')
        else:
            flash('Book returned successfully on time! Thank you.', 'success')

    except Exception as e:
        db.session.rollback()
        flash(f'Error processing return: {str(e)}', 'danger')

    return redirect(url_for('student.dashboard'))


@student_bp.route('/history')
@login_required
def history():
    """Complete borrowing history for the current student."""
    settings = LibrarySettings.get_settings()
    status_filter = request.args.get('status', 'all')
    page = request.args.get('page', 1, type=int)

    query = Loan.query.filter_by(user_id=current_user.id)

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

    return render_template('student/history.html',
                           loans=loans,
                           pagination=pagination,
                           status_filter=status_filter,
                           daily_fine_rate=settings.daily_fine_rate)
