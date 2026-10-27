from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models import db, User
from app.forms import LoginForm, RegistrationForm

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Handles new user/student registration."""
    if current_user.is_authenticated:
        return redirect(url_for('student.dashboard' if not current_user.is_admin else 'admin.dashboard'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            name=form.name.data.strip(),
            email=form.email.data.strip().lower(),
            role='student'  # Registration default is always student
        )
        user.set_password(form.password.data)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Account registered successfully! You can now log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Handles user/admin authentication."""
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard' if current_user.is_admin else 'student.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.strip().lower()).first()
        
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(f'Welcome back, {user.name}!', 'success')
            
            # Safe redirection to next_page
            next_page = request.args.get('next')
            if not next_page or not next_page.startswith('/'):
                if user.is_admin:
                    next_page = url_for('admin.dashboard')
                else:
                    next_page = url_for('student.dashboard')
            return redirect(next_page)
        else:
            flash('Invalid email or password. Please verify your credentials.', 'danger')

    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    """Logs out the active user and clears session."""
    logout_user()
    flash('You have been logged out securely.', 'info')
    return redirect(url_for('main.index'))
