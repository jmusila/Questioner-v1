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

@api.route('/<int:m_id>/questions')
class Questions(Resource):

    @api.expect(new_question, validate = True)
    def post(self, m_id):
        '''Post a question'''
        a = meetup.get_single_meetup(m_id)
        if a:
            new_qsn = api.payload
            new_qsn['qsn_id'] = len(new_qsn) + 1
            new_qsn['createdOn'] = question.createdOn
            new_qsn['meetup_id'] = a['m_id']
            question.Questions.append(new_qsn)
            return {'Message': "Question added successfully", 'Status': 201}, 201
        raise NotFound ('Meetup with that id not found')