import logging
import os

from app import db
from app.db.models import User, Transaction

def test_balance(application, client):

    with application.app_context():
        user = {'email': '1234@gmail.com','password': '123456','balance':'0'}
        client.post("/register", data=user)

        user_2 ={'email': '1234@gmail.com','password': '123456'}

        client.post("/login",data = user_2)
        root = os.path.dirname(os.path.abspath(__file__))
        testdir = os.path.join(root, '../tests')
        assert os.path.exists(testdir) == True

        test_file = os.path.join(testdir, 't4.csv')
        assert os.path.exists(test_file) == True
        upload_dir = os.path.join(root, '../app/uploads')
        #assert os.path.exists(upload_dir)

        test_file_2 ={
            'file' : open(test_file,'rb')
        }
        responce = client.post('/app/uploads', data = test_file_2)
        assert responce.status_code == 404
        #assert user.balance == 200.00

       # assert len(os.listdir(upload_dir)) == 0
