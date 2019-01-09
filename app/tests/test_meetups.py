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

    def test_get_single_meetup(self):
        """Test API can get a single meetup by using it's id."""
        rv = self.client.post('/meetups/upcoming', data=json.dumps(self.meetup), content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        rv1 = self.client.get('/meetups/upcoming/1')
        data = json.loads(rv1.data.decode())
        self.assertEqual(rv1.status_code, 200)
        self.assertIn('PAC', str(rv1.data))

    def test_get_all_meetups(self):
        res = self.client.post('/meetups/upcoming', data=json.dumps(self.meetup), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res1 = self.client.get('/meetups/upcoming')
        data = json.loads(res1.get_data().decode())
        self.assertEqual(res1.status_code, 200)
        self.assertIn('Python', str(res1.data))

    def test_get_meetup_id_that_doesnt_exist(self):
        res = self.client.post('/meetups/upcoming', data=json.dumps(self.meetup), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res1 = self.client.get('/meetups/upcoming/4') 
        data = json.loads(res1.get_data().decode())
        self.assertEqual(res1.status_code, 404)