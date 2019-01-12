"""
This file contains all the routes
"""

# Third party imports
from flask import Blueprint
from flask_restplus import Api

#Local imports
from .views.meetups import api as meetups_route
from .views.questions import api as questions_route
from .views.rsvp import api as response_route


version1 = Blueprint('api', __name__, url_prefix="/api/v1")
api = Api(version1)
api = Api(
    title ='Questioner',
    version='1.0',
    description='A simple Questioner API',
)

api.add_namespace(meetups_route, path = "/api/v1/meetups/upcoming")
api.add_namespace(questions_route, path = "/api/v1/meetups")
api.add_namespace(response_route, path = "/api/v1/meetups")