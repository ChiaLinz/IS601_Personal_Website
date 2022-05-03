import os

def test_upload_file(application, client):

    with application.app_context():
        data = {
            'email': '123@gmail.com',
            'password': '123456',
            'confirm': '123456'
        }
        client.post("/register", data=data)

        data2 ={
            'email': '123@gmail.com',
            'password': '123456'

        }

        client.post("/login",data = data2)
        root = os.path.dirname(os.path.abspath(__file__))
        testdir = os.path.join(root, '../tests')
        assert os.path.exists(testdir) == True

        test_file = os.path.join(testdir, 'test.csv')
        assert os.path.exists(test_file) == True
