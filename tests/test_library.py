import unittest
from datetime import date, timedelta
from app import create_app
from app.models import db, User, Book, Loan, LibrarySettings

class LibraryTestCase(unittest.TestCase):
    def setUp(self):
        """Set up in-memory test database and client."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        
        db.create_all()
        
        # Create Library Settings
        self.settings = LibrarySettings.get_settings()
        
        # Create Admin
        self.admin = User(name='Admin Test', email='admin@test.com', role='admin')
        self.admin.set_password('AdminPass123')
        db.session.add(self.admin)
        
        # Create Student 1
        self.student1 = User(name='Student One', email='student1@test.com', role='student')
        self.student1.set_password('StudentPass123')
        db.session.add(self.student1)

        # Create Student 2
        self.student2 = User(name='Student Two', email='student2@test.com', role='student')
        self.student2.set_password('StudentPass123')
        db.session.add(self.student2)

        # Create Books
        self.book1 = Book(
            title='Python Testing',
            author='Test Author',
            isbn='9781111111111',
            category='Programming',
            publication_year=2021,
            total_copies=2,
            available_copies=2
        )
        self.book_single = Book(
            title='Single Copy Book',
            author='Rare Author',
            isbn='9782222222222',
            category='Literature',
            publication_year=2020,
            total_copies=1,
            available_copies=1
        )
        db.session.add_all([self.book1, self.book_single])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def login(self, email, password):
        return self.client.post('/auth/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.client.get('/auth/logout', follow_redirects=True)

    # 1. Registration and Login Test
    def test_registration_and_login(self):
        response = self.client.post('/auth/register', data=dict(
            name='New Student',
            email='newstudent@test.com',
            password='Password123',
            confirm_password='Password123'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Account registered successfully', response.data)

        # Verify user exists
        user = User.query.filter_by(email='newstudent@test.com').first()
        self.assertIsNotNone(user)
        self.assertTrue(user.check_password('Password123'))

        # Login
        login_res = self.login('newstudent@test.com', 'Password123')
        self.assertIn(b'New Student', login_res.data)

    # 2. Unauthorized Admin Access
    def test_unauthorized_admin_access(self):
        # Student tries to access admin dashboard
        self.login('student1@test.com', 'StudentPass123')
        response = self.client.get('/admin/dashboard', follow_redirects=True)
        self.assertIn(b'Access denied: Administrator privileges required', response.data)

        # Unauthenticated user tries to access admin dashboard
        self.logout()
        res_unauth = self.client.get('/admin/dashboard', follow_redirects=True)
        self.assertIn(b'Please log in', res_unauth.data)

    # 3. Add and Search Books
    def test_search_books(self):
        # Search by title
        res = self.client.get('/catalog?q=Python')
        self.assertIn(b'Python Testing', res.data)
        self.assertNotIn(b'Single Copy Book', res.data)

        # Search by category
        res_cat = self.client.get('/catalog?category=Literature')
        self.assertIn(b'Single Copy Book', res_cat.data)

    # 4. Issuing an Available Book & Stock Decrement
    def test_issue_book_success(self):
        self.login('student1@test.com', 'StudentPass123')
        response = self.client.post(f'/student/issue/{self.book1.id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Successfully issued', response.data)

        # Stock should decrease from 2 to 1
        book = Book.query.get(self.book1.id)
        self.assertEqual(book.available_copies, 1)

        # Loan record created
        loan = Loan.query.filter_by(user_id=self.student1.id, book_id=self.book1.id, status='issued').first()
        self.assertIsNotNone(loan)
        self.assertEqual(loan.due_date, date.today() + timedelta(days=14))

    # 5. Prevent Issue When Stock is Zero
    def test_prevent_issue_when_zero_stock(self):
        # Student 1 issues the only copy
        self.login('student1@test.com', 'StudentPass123')
        self.client.post(f'/student/issue/{self.book_single.id}', follow_redirects=True)
        self.logout()

        # Stock is now 0
        book = Book.query.get(self.book_single.id)
        self.assertEqual(book.available_copies, 0)

        # Student 2 attempts to issue the same book
        self.login('student2@test.com', 'StudentPass123')
        res = self.client.post(f'/student/issue/{self.book_single.id}', follow_redirects=True)
        self.assertIn(b'out of stock', res.data)

    # 6. Return Book & Stock Increment
    def test_return_book(self):
        self.login('student1@test.com', 'StudentPass123')
        self.client.post(f'/student/issue/{self.book1.id}', follow_redirects=True)
        
        loan = Loan.query.filter_by(user_id=self.student1.id, book_id=self.book1.id, status='issued').first()
        self.assertIsNotNone(loan)

        # Process return
        return_res = self.client.post(f'/student/return/{loan.id}', follow_redirects=True)
        self.assertIn(b'Book returned successfully', return_res.data)

        # Stock restored
        book = Book.query.get(self.book1.id)
        self.assertEqual(book.available_copies, 2)

        # Duplicate return prevention
        dup_res = self.client.post(f'/student/return/{loan.id}', follow_redirects=True)
        self.assertIn(b'already been marked as returned', dup_res.data)

    # 7. Late Fine Calculation (On time vs 5 days overdue)
    def test_late_fine_calculation(self):
        self.login('student1@test.com', 'StudentPass123')
        self.client.post(f'/student/issue/{self.book1.id}', follow_redirects=True)
        
        loan = Loan.query.filter_by(user_id=self.student1.id, book_id=self.book1.id, status='issued').first()
        
        # Case A: On time return (Fine should be 0)
        self.assertEqual(loan.calculate_current_fine(daily_rate=5.0), 0.0)

        # Case B: Simulate 5 days overdue
        loan.due_date = date.today() - timedelta(days=5)
        db.session.commit()

        self.assertTrue(loan.is_overdue)
        self.assertEqual(loan.overdue_days, 5)
        # 5 days * 5.0 rate = 25.0
        self.assertEqual(loan.calculate_current_fine(daily_rate=5.0), 25.0)

    # 8. Prevent Student From Accessing Another Student's Return Action
    def test_prevent_cross_user_return(self):
        # Student 1 issues book
        self.login('student1@test.com', 'StudentPass123')
        self.client.post(f'/student/issue/{self.book1.id}', follow_redirects=True)
        loan = Loan.query.filter_by(user_id=self.student1.id, book_id=self.book1.id).first()
        self.logout()

        # Student 2 tries to return Student 1's book
        self.login('student2@test.com', 'StudentPass123')
        res = self.client.post(f'/student/return/{loan.id}', follow_redirects=True)
        self.assertIn(b'Unauthorized: You cannot return a loan belonging to another user', res.data)

    # 9. Admin Dashboard Statistics
    def test_admin_dashboard_metrics(self):
        self.login('admin@test.com', 'AdminPass123')
        res = self.client.get('/admin/dashboard')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Administrator Dashboard', res.data)
        self.assertIn(b'Catalogue Titles', res.data)

if __name__ == '__main__':
    unittest.main()
