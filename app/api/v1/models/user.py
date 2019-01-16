from datetime import datetime
from flask import make_response, jsonify, request

Users =[]

class User:
    """ User constructor method """
    def __init__(self, fname=None, lname=None, email=None, username=None, password=None, registered=None, isAdmin=None):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.username = username
        self.password = password
        self.registered = datetime.now()
        self.isAdmin = False 

    def add_new_user(self, person):
        new_user ={
        "user_id": person['user_id'],
        "fname": person['fname'],
        "lname": person['lname'],
        "email": person['email'],
        "password": person['password'],
        "username": person['username'],
        "registered": str(datetime.now()),
        "isAdmin":person['isAdmin']
        }

        Users.append(new_user)


    """ Method for getting a single user """
    def check_exists(self, person):
    	for i in Users:
    		if i['username'] == person['username'] or i['email'] == person['email']:
    			return {'Message': "Username or email already taken"}, 409

    def get_single_user(self, user_id):
        for item in Users:
            if item['user_id'] == user_id:
                return item
            return {'Message': "User with that id not found"}, 404








        