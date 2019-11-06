import re

#Third party imports
from flask_restplus import Resource
from flask import request, abort, jsonify, make_response

#Local imports
from app.api.v1.models.user import User, Users
from app.api.v1.views.expect import UserModel

user = User()
new_user = UserModel().users
api = UserModel().api 

@api.route('/register')
class AuthRegister(Resource):
    @api.doc('list_users')
    @api.marshal_with(new_user, envelope = 'Users')
    def get(self):
        '''List all users'''
        return Users, 200

    @api.expect(new_user, validate = True)
    def post(self):
        '''Register a user'''
        data = request.get_json()
        email_format = re.compile(r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[.a-zA-Z-]+$)")
        person ={
            "user_id": int(len(Users)+ 1),
            "fname": data['fname'],
            "lname": data['lname'],
            "username": data['username'],
            "email": data['email'],
            "password": data['password'], 
            "registered": user.registered,
            "isAdmin": user.isAdmin
        }
        if len(person['password']) < 8:
            return {'message': 'Password should be at least 8 characters'}, 400
        elif not (re.match(email_format, person['email'])):
            return {'message': 'Invalid email'}, 400
        elif len(person['username']) < 4:
            return {'message': 'Username too short'}
        else:
        # Check if the item is not required
            for item in data.keys():
                if item not in person:
                    return {"message": "The field '{}' is not required for registration".format(item)}, 400
        confli = user.check_exists(person)
        if confli:
            return confli

        user.add_new_user(person) 
        return make_response(jsonify({'Message': "{} registered successfully".format(data['email']), "username": data['username']}), 201)

@api.route('/login')
class AuthLogin(Resource):
    @api.expect(new_user)
    def post(self):
        ''' Login a registered user '''
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        for person in Users:
            if (person["email"] == email) and person["password"] == password:
                return {'Message': "{} logged in successfully".format(data['email'])}, 200
            else:
                return {"message": "Enter correct username or password"}, 404
            return {"message": "Enter correct username or password"}, 404


        


