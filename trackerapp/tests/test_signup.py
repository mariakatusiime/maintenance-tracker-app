            
import unittest

from trackerapp.models.user_views import app


import json


import sys

class tddonsignup(unittest.TestCase):
    def setUp(self):
        self.app= app.test_client()
        self.userdetails={
            "fname":"maria",
            "sname":"kats",
            "username":"maria",
            "password":"password",
            "rpassword":"rpassword",
            "email":"email",
            "dept":"dept",
        }


    def test_usersignupdetailsareinput(self):
        #response=self.app.post('/users',data=json.dumps(self.userdetails))
        response=self.app.post('/users',data=json.loads(response.get_data(self.userdetails).decode(sys.getdefaultencoding())))
        self.assertEqual(response.status_code, 201)
        
        #self.assertIn("Succefully signup",str(feedback.data))
        

    if __name__ == '__main__':
        unittest.main()


        