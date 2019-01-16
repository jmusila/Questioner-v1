import unittest
import json

#local imports
from app.apps import create_app
from .base_test import Settings

class TestQuestions(Settings):

    def test_register_user(self):
        """Test API can create a new user to questioner"""
        res = self.client.post('api/v1/auth/register', content_type='application/json', data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)

    def test_get_all_users(self):
        """Test API can get all the users from the list."""
        res = self.client.post('api/v1/auth/register', content_type='application/json', data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)
        rv1 = self.client.get('api/v1/auth/register')
        data = json.loads(rv1.data.decode())
        self.assertEqual(rv1.status_code, 200)
        self.assertIn('jonathan', str(rv1.data))

    def test_login_user(self):
        """Test API can create a new user to questioner"""
        res = self.client.post('api/v1/auth/login', data=json.dumps(self.login), content_type='application/json')
        self.assertEqual(res.status_code, 200)