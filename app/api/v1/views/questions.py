"""
This file contaions all the endpoints for the questions

"""

# Third party imports
from flask_restplus import Resource
from flask import request, make_response, jsonify
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized, Forbidden

#Local imports
from app.api.v1.models.questions import Question
from app.api.v1.views.expect import QuestionModel
from app.api.v1.models.meetups import Meetups
from app.api.v1.views.meetups import meetup

question = Question('qsn_id', 'body','meetup_id', 'title', 'votes' )
new_question = QuestionModel().questions
api = QuestionModel().api 