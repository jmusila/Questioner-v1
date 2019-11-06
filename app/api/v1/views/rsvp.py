# Third party imports
from flask_restplus import Resource
from flask import request, make_response, jsonify

#Local imports
from app.api.v1.models.rsvp import Responds, Responses
from app.api.v1.views.expect import ResponseModel
from app.api.v1.models.meetups import Meetup
from app.api.v1.views.meetups import meetup

response = Responds()
new_res = ResponseModel().responses
api = ResponseModel().api

@api.route('/<int:m_id>/rsvp')
class ReapondOp(Resource):

    @api.expect(new_res, validate = True)
    def post(self, m_id):
        '''Post a question'''
        a = meetup.get_single_meetup(m_id)
        if a:
            data = request.get_json()
            res ={
                "r_id": int(len(Responses)+ 1),
                "meetup_id": a['m_id'],
                "topic": a['topic'],
                "status": data['status']  
            }
            response.add_new_response(res)
            return make_response(jsonify({'Message': "Response added successfully", 'Status': 201, "Data": res}), 201)
        return make_response(jsonify({'Message': "Meetup with that id not found", 'Status': 404}), 404)