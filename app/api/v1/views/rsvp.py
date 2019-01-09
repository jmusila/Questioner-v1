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