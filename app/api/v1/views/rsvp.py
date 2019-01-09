# Third party imports
from flask_restplus import Resource
from flask import request, make_response, jsonify
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized, Forbidden

#Local imports
from app.api.v1.models.rsvp import Responds
from app.api.v1.views.expect import ResponseModel
from app.api.v1.models.meetups import Meetups
from app.api.v1.views.meetups import meetup

response = Responds('r_id', 'meetup_id', 'topic', 'status' )
new_res = ResponseModel().responses
api = ResponseModel().api

@api.route('/<int:m_id>/rsvp')
class ReapondOp(Resource):

    @api.expect(new_res, validate = True)
    def post(self, m_id):
        '''Post a question'''
        a = meetup.get_single_meetup(m_id)
        if a:
            new_response = api.payload
            new_response['r_id'] = len(response.Responds) + 1
            new_response['meetup_id'] = a['m_id']
            new_response['topic'] = a['topic']
            response.Responds.append(new_response)
            return make_response(jsonify({'Message': "Response added successfully", 'Status': 201, "Data": new_response}), 201)
        raise NotFound ('Meetup with that id not found')