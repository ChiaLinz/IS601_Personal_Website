from app import db
from app.db.models import User, Transaction

def test_add_user(application):
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
        user = User(email='123@gmail.com', password='123456')
        db.session.add(user)
        user = User.query.filter_by(email='123@gmail.com').first()
        assert user.password == '123456'
        assert db.session.query(User).count() == 1


def test_upload_transaction(application):
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
        user = User(email='123@gmail.com', password='123456')
        db.session.add(user)
        user.transaction = [Transaction(100,'CREDIT')]
        assert db.session.query(Transaction).count() == 0

