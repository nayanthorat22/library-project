from flask import Blueprint, render_template, request
from app.models import Book, LibrarySettings

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Home landing page with quick statistics and featured books."""
    total_books = Book.query.count()
    available_books = Book.query.filter(Book.available_copies > 0).count()
    featured_books = Book.query.order_by(Book.created_at.desc()).limit(6).all()
    return render_template('main/index.html', 
                           total_books=total_books, 
                           available_books=available_books, 
                           featured_books=featured_books)


@main_bp.route('/catalog')
def catalog():
    """
    Searchable and filterable book catalog.
    Supports filtering by query, category, and availability status.
    """
    query = request.args.get('q', '').strip()
    category = request.args.get('category', '').strip()
    availability = request.args.get('availability', '').strip()
    page = request.args.get('page', 1, type=int)

    books_query = Book.query

    # Search filter across Title, Author, ISBN, or Category
    if query:
        search_pattern = f"%{query}%"
        books_query = books_query.filter(
            (Book.title.ilike(search_pattern)) |
            (Book.author.ilike(search_pattern)) |
            (Book.isbn.ilike(search_pattern)) |
            (Book.category.ilike(search_pattern))
        )

    # Category filter
    if category:
        books_query = books_query.filter(Book.category == category)

    # Availability filter
    if availability == 'available':
        books_query = books_query.filter(Book.available_copies > 0)
    elif availability == 'out_of_stock':
        books_query = books_query.filter(Book.available_copies == 0)

    # Pagination: 9 books per page
    pagination = books_query.order_by(Book.title.asc()).paginate(page=page, per_page=9, error_out=False)
    books = pagination.items

    # List of all unique categories for the dropdown filter
    all_categories = [c[0] for c in Book.query.with_entities(Book.category).distinct().order_by(Book.category).all()]

    return render_template('main/catalog.html',
                           books=books,
                           pagination=pagination,
                           query=query,
                           category=category,
                           availability=availability,
                           categories=all_categories)


@main_bp.route('/book/<int:book_id>')
def book_detail(book_id):
    """Detailed view for an individual book."""
    book = Book.query.get_or_404(book_id)
    settings = LibrarySettings.get_settings()
    return render_template('main/book_detail.html', book=book, settings=settings)
