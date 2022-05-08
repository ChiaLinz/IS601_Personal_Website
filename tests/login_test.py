import os
from pathlib import Path
from app import db
from app.db.models import User

def test_register(application):
    with application.app_context():
        assert db.session.query(User).count() == 0
        user = User(email='123@gmail.com', password='123456')
        db.session.add(user)
        user = User.query.filter_by(email='123@gmail.com').first()
        assert user.password == '123456'
        assert db.session.query(User).count() == 1

def test_login(client):
    data = {'email': "123@gmail.com", 'password': "123456", 'confirm': "123456"}
    client.post('/register', data=data)
    data = {'email': "123@gmail.com", 'password': "123456",}
    client.post('/login', data=data)
    response = client.get('/dashboard')
    assert response.status_code == 302
