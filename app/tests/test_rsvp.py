import unittest
import json

#local imports
from app.apps import create_app
from .base_test import Settings

class TestQuestions(Settings):

    def test_post_response(self):
        """Test API can post a response to a tagged meetup """
        res = self.client.post('/meetups/upcoming', data=json.dumps(self.meetup), content_type='application/json')
        rv = self.client.post('/meetups/1/rsvp', data=json.dumps(self.rsvp), content_type='application/json')
        self.assertEqual(res.status_code, 201)