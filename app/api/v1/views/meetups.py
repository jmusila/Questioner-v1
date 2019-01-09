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

@api.route('')
class Meetup(Resource):
    @api.doc('list_meetups')
    def get(self):

    @api.expect(new_meetup, validate = True)
    def post(self):
        '''Post a meetup'''
        new_mtup = api.payload
        new_mtup['m_id'] = len(meetup.Meetups) + 1
        new_mtup['createdOn'] = meetup.createdOn
        meetup.Meetups.append(new_mtup)
        return make_response(jsonify({'Message': "Meetup added successfully", 'Status': 201, "data":new_mtup}), 201)

@api.route('/<int:m_id>')
class SingleMeetup(Resource):
    @api.marshal_with(new_meetup, envelope = 'Meetup')
    def get(self, m_id):
        '''Get single Meetup'''
        a = meetup.get_single_meetup(m_id)
        if a:
            return a
        raise NotFound ('Meetup with that id not found')