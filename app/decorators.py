from functools import wraps
from flask import abort, flash, redirect, url_for
from flask_login import current_user

def admin_required(f):
    """
    Decorator for protecting admin-only endpoints.
    Ensures user is logged in AND possesses the 'admin' role.
    If unauthorized, aborts with 403 Forbidden or redirects with alert.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('Please log in first to access this page.', 'warning')
            return redirect(url_for('auth.login'))
        if not current_user.is_admin:
            flash('Access denied: Administrator privileges required.', 'danger')
            return redirect(url_for('student.dashboard'))
        return f(*args, **kwargs)
    return decorated_function
