"""
This file contains all the routes
"""

# Third party imports
from flask import Blueprint
from flask_restplus import Api

#Local imports
from .views.meetups import api as meetups_route
from .views.questions import api as questions_route

version1 = Blueprint('api', __name__, url_prefix="/api/v1")
api = Api(version1)
api = Api(
    title ='Questioner',
    version='1.0',
    description='A simple Questioner API',
)

api.add_namespace(meetups_route, path = "/meetups/upcoming")