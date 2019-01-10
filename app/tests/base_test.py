"""
This will contain the base tests configuration.
Thi will be reused/imported in almost all the tests.

"""
# Standard library imports
import unittest
import json

# Local application imports
from app.apps import create_app

class Settings(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

        self.meetup ={
            "m_id":1,
            "createdOn":"Wed, 09 Jan 2019 22:19:25 GMT",
            "location": "PAC",
            "images": "images",
            "topic": "Python",
            "happeningOn": "12th Feb"
        }

        self.question ={
            "body": "The question body",
            "createdOn": "Wed, 09 Jan 2019 23:10:16 GMT",
            "meetup_id": 1,
            "qsn_id": 1,
            "title": "question title",
            "votes": 2
        }

    def tearDown(self):
        del self.meetup
        del self.question