import unittest
from app import app  # Assuming your Flask application is defined in 'app.py'
from dotenv import load_dotenv

try:
    load_dotenv()  # Load environment variables from .env file
except Exception as e:
    print("Missing modules {}".format(e))

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        # set up test client
        self.app = app.test_client(self)
        self.app.testing = True

    def test_home_page(self):
        # send a GET request to the home page
        result = self.app.get('/')
        # check that the status code is 200 (OK)
        self.assertEqual(result.status_code, 200)
        # check that the response content contains the expected message
        # self.assertIn(b'Hello, World!', result.data)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()

