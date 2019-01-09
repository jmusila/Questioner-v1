#Third party imports
from flask_restplus import Resource
from flask import request, make_response, jsonify
from werkzeug.exceptions import NotFound

#Local imports
from app.api.v1.models.meetups import Meetups
from app.api.v1.views.expect import MeetupsModel

meetup = Meetups('m_id', 'location', 'images', 'topic', 'happeningOn')
new_meetup = MeetupsModel().meetups
api = MeetupsModel().api