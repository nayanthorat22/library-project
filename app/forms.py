from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField, FloatField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, NumberRange
from app.models import User, Book

class RegistrationForm(FlaskForm):
    """User and Student registration form."""
    name = StringField('Full Name', validators=[
        DataRequired(message="Name is required."),
        Length(min=2, max=100, message="Name must be between 2 and 100 characters.")
    ])
    email = StringField('Email Address', validators=[
        DataRequired(message="Email is required."),
        Email(message="Please enter a valid email address.")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message="Password is required."),
        Length(min=6, message="Password must be at least 6 characters long.")
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(message="Please confirm your password."),
        EqualTo('password', message="Passwords must match.")
    ])
    submit = SubmitField('Register Account')

    def validate_email(self, field):
        """Validates that email is unique."""
        if User.query.filter_by(email=field.data.lower().strip()).first():
            raise ValidationError('This email address is already registered. Please log in or use another email.')


class LoginForm(FlaskForm):
    """User and Admin login form."""
    email = StringField('Email Address', validators=[
        DataRequired(message="Email is required."),
        Email(message="Please enter a valid email address.")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message="Password is required.")
    ])
    submit = SubmitField('Sign In')


class BookForm(FlaskForm):
    """Form to add or edit books (Admin only)."""
    title = StringField('Book Title', validators=[
        DataRequired(message="Book title is required."),
        Length(max=200)
    ])
    author = StringField('Author', validators=[
        DataRequired(message="Author name is required."),
        Length(max=150)
    ])
    isbn = StringField('ISBN Number', validators=[
        DataRequired(message="ISBN is required."),
        Length(min=5, max=20, message="ISBN should be 5-20 characters.")
    ])
    category = StringField('Category / Genre', validators=[
        DataRequired(message="Category is required."),
        Length(max=80)
    ])
    publication_year = IntegerField('Publication Year', validators=[
        DataRequired(message="Publication year is required."),
        NumberRange(min=1000, max=2100, message="Enter a valid 4-digit year.")
    ])
    total_copies = IntegerField('Total Copies', validators=[
        DataRequired(message="Total copies count is required."),
        NumberRange(min=1, max=1000, message="Total copies must be between 1 and 1000.")
    ])
    description = TextAreaField('Description / Synopsis', validators=[
        Length(max=2000)
    ])
    submit = SubmitField('Save Book')

    def __init__(self, original_isbn=None, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.original_isbn = original_isbn

    def validate_isbn(self, field):
        """Prevents duplicate ISBN registration."""
        cleaned_isbn = field.data.strip()
        if self.original_isbn and cleaned_isbn == self.original_isbn:
            return
        if Book.query.filter_by(isbn=cleaned_isbn).first():
            raise ValidationError('A book with this ISBN already exists in the catalogue.')


class SettingsForm(FlaskForm):
    """Form to configure library parameters."""
    borrow_duration_days = IntegerField('Loan Duration (Days)', validators=[
        DataRequired(),
        NumberRange(min=1, max=180, message="Loan duration must be between 1 and 180 days.")
    ])
    daily_fine_rate = FloatField('Daily Fine Rate (₹)', validators=[
        DataRequired(),
        NumberRange(min=0.0, max=500.0, message="Daily fine cannot be negative.")
    ])
    max_borrow_limit = IntegerField('Max Books Per User', validators=[
        DataRequired(),
        NumberRange(min=1, max=20, message="Borrow limit must be between 1 and 20 books.")
    ])
    submit = SubmitField('Update Library Rules')
