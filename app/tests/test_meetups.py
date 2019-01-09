import unittest
import json

#local imports
from app.apps import create_app
from .base_test import Settings

class TestMeetups(Settings):

    def test_post_meetup(self):
    """Test API can post a meetup"""
    res = self.client.post('/meetups/upcoming', content_type='application/json', data=json.dumps(self.meetup))
    self.assertEqual(res.status_code, 201)