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
from app.api.v1.views.expect import VotesModel

question = Question('qsn_id', 'body','meetup_id', 'title', 'votes' )
new_question = QuestionModel().questions
n_votes = VotesModel().nvotes
api = QuestionModel().api 

@api.route('/<int:m_id>/questions')
class Questions(Resource):

    @api.expect(new_question, validate = True)
    def post(self, m_id):
        '''Post a question'''
        a = meetup.get_single_meetup(m_id)
        if a:
            new_qsn = api.payload
            new_qsn['qsn_id'] = len(question.Questions) + 1
            new_qsn['createdOn'] = question.createdOn
            new_qsn['meetup_id'] = a['m_id']
            question.Questions.append(new_qsn)
            return make_response(jsonify({'Message': "Question added successfully", 'Status': 201, "Data": new_qsn}), 201)
        raise NotFound ('Meetup with that id not found')

@api.route('/<int:m_id>/questions/<int:qsn_id>')
class SingleQuestion(Resource):
    @api.marshal_with(new_question, envelope = 'Question')
    def get(self, m_id, qsn_id):
        '''Get single Question'''
        if meetup.get_single_meetup(m_id):
            a = question.get_single_question(qsn_id)
            if a:
                return a
            raise NotFound ('Question with that id not found')
        raise NotFound ('Meetup with that id not found')

    @api.expect(new_question, validate = True)
    def put(self, m_id, qsn_id):
        '''Update Question'''
        if meetup.get_single_meetup(m_id):
            u = api.payload
            q = question.get_single_question(qsn_id)
            if q:
                u['meetup_id'] = q['meetup_id']
                u['qsn_id'] = q['qsn_id']
                q.update(u)
                return make_response(jsonify({'Message': "Question updated successfully", 'Status': 201, "Data":u}), 201)
            raise NotFound('Question with that id not found')
        raise NotFound('Meetup with that id not found')

@api.route('/questions/<int:qsn_id>/upvote')
class UpVoteQuestion(Resource):
    @api.expect(n_votes, validate = True)
    def patch(self, qsn_id):
        ''' Up votes '''
        item = question.get_single_question(qsn_id)
        if item:
            item['votes'] = item['votes']+ 1
            return make_response(jsonify({'Message': "Vote updated successfully", 'Status': 201, "Data": item}), 201)
        raise NotFound ('Question with that id not found')

@api.route('/questions/<int:qsn_id>/downvote')
class DownVoteQuestion(Resource):
    @api.expect(n_votes, validate = True)
    def patch(self, qsn_id):
        ''' Down votes '''
        item = question.get_single_question(qsn_id)
        if item:
            if item['votes'] > 0: 
                item['votes'] = item['votes']- 1
                return make_response(jsonify({'Message': "Vote updated successfully", 'Status': 201, "Data": item}), 201)
            raise BadRequest('Votes cannot be less than zero')
        raise NotFound ('Question with that id not found')
