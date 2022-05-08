import os
from pathlib import Path

from app.db.models import User

def test_user_upload_reject(client):
    data = {
        'email': "123@gmail.com",
        'password': "123456",
        'confirm': "123456"
    }
    client.post('/register', data=data)
    data = {
        'email': "123@gmail.com",
        'password': "123456",
    }
    client.post('/login', data=data)
    root = os.path.dirname(os.path.abspath(__file__))
    testdir = os.path.join(root, '../tests')
    test_file = os.path.join(testdir, 'test.txt')
    upload_dir = os.path.join(root, '../uploads')
    if not os.path.exists(upload_dir):
        os.mkdir(upload_dir)
    if len(os.listdir(upload_dir)) != 0:
        for file in os.listdir(upload_dir):
            os.remove(str(upload_dir) + '/' + file)
    assert len(os.listdir(upload_dir)) == 0
    data = {
        'file': open(test_file, 'rb')
    }
    response = client.post('/transactions/upload', data=data)
    assert b'' in response.data
    for file in os.listdir(upload_dir):
        os.remove(str(upload_dir) + '/' + file)