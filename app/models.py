from datetime import datetime, date, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(UserMixin, db.Model):
    """
    User model representing both Students and Administrators.
    Uses role-based access ('student' or 'admin').
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='student')  # 'student' or 'admin'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    loans = db.relationship('Loan', back_populates='user', cascade='all, delete-orphan', lazy='dynamic')

    @property
    def is_admin(self):
        return self.role == 'admin'

    def set_password(self, password):
        """Hashes the password with Werkzeug salt & hash."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifies given password against stored hash."""
        return check_password_hash(self.password_hash, password)

    def get_active_loans_count(self):
        """Returns number of books currently issued to this user."""
        return self.loans.filter_by(status='issued').count()

    def __repr__(self):
        return f'<User {self.email} ({self.role})>'


class Book(db.Model):
    """
    Book model for library catalogue management.
    Ensures total_copies and available_copies consistency.
    """
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, index=True)
    author = db.Column(db.String(150), nullable=False, index=True)
    isbn = db.Column(db.String(20), unique=True, nullable=False, index=True)
    category = db.Column(db.String(80), nullable=False, index=True)
    publication_year = db.Column(db.Integer, nullable=True)
    total_copies = db.Column(db.Integer, nullable=False, default=1)
    available_copies = db.Column(db.Integer, nullable=False, default=1)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    loans = db.relationship('Loan', back_populates='book', lazy='dynamic')

    @property
    def is_available(self):
        return self.available_copies > 0

    def has_active_loans(self):
        """Checks if book is currently checked out by anyone."""
        return self.loans.filter_by(status='issued').count() > 0

    def __repr__(self):
        return f'<Book {self.title} by {self.author} (ISBN: {self.isbn})>'


class Loan(db.Model):
    """
    Loan model tracking borrowing transactions, due dates, returns, and late fines.
    Never deleted when books are returned, maintaining complete historical records.
    """
    __tablename__ = 'loans'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id', ondelete='RESTRICT'), nullable=False, index=True)
    issue_date = db.Column(db.Date, nullable=False, default=date.today)
    due_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(20), nullable=False, default='issued')  # 'issued', 'returned'
    
    # Financial fine attributes
    calculated_fine = db.Column(db.Float, nullable=False, default=0.0)
    fine_paid = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user = db.relationship('User', back_populates='loans')
    book = db.relationship('Book', back_populates='loans')

    def calculate_current_fine(self, daily_rate=5.0):
        """
        Calculates overdue fine based on due date.
        - If returned: calculates difference between return_date and due_date.
        - If not returned: calculates difference between today and due_date.
        - Guaranteed to never return negative numbers.
        """
        effective_end_date = self.return_date if self.return_date else date.today()
        if effective_end_date > self.due_date:
            overdue_days = (effective_end_date - self.due_date).days
            return round(overdue_days * daily_rate, 2)
        return 0.0

    @property
    def overdue_days(self):
        """Returns the number of overdue days (0 if on time)."""
        effective_end_date = self.return_date if self.return_date else date.today()
        if effective_end_date > self.due_date:
            return (effective_end_date - self.due_date).days
        return 0

    @property
    def is_overdue(self):
        """Checks if loan is past its due date without being returned or returned late."""
        if self.status == 'issued':
            return date.today() > self.due_date
        return self.return_date is not None and self.return_date > self.due_date

    def __repr__(self):
        return f'<Loan User:{self.user_id} Book:{self.book_id} Status:{self.status}>'


class LibrarySettings(db.Model):
    """
    Configurable rules for library operations:
    - Borrowing duration in days
    - Daily late fine amount (₹)
    - Maximum books a user can hold simultaneously
    """
    __tablename__ = 'library_settings'

    id = db.Column(db.Integer, primary_key=True)
    borrow_duration_days = db.Column(db.Integer, nullable=False, default=14)
    daily_fine_rate = db.Column(db.Float, nullable=False, default=5.0)
    max_borrow_limit = db.Column(db.Integer, nullable=False, default=3)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @classmethod
    def get_settings(cls):
        """Retrieves the singleton library settings row or initializes default."""
        settings = cls.query.first()
        if not settings:
            settings = cls(
                borrow_duration_days=14,
                daily_fine_rate=5.0,
                max_borrow_limit=3
            )
            db.session.add(settings)
            db.session.commit()
        return settings

    def __repr__(self):
        return f'<LibrarySettings duration={self.borrow_duration_days}d fine=₹{self.daily_fine_rate}/d>'
