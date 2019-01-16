"""
This file contaions all the endpoints for the questions

"""

# Third party imports
from flask_restplus import Resource
from flask import request, make_response, jsonify

#Local imports
from app.api.v1.models.questions import Question, Questions
from app.api.v1.views.expect import QuestionModel
from app.api.v1.models.meetups import Meetup
from app.api.v1.views.meetups import meetup
from app.api.v1.views.expect import VotesModel

question = Question()
new_question = QuestionModel().questions
n_votes = VotesModel().nvotes
api = QuestionModel().api 

@api.route('/<int:m_id>/questions')
class QuestionsOp(Resource):

    @api.expect(new_question, validate = True)
    def post(self, m_id):
        '''Post a question'''
        a = meetup.get_single_meetup(m_id)
        if a:
            data = request.get_json()
            new_q ={
            "qsn_id": int(len(Questions)+ 1),
            "meetup_id": a['m_id'],
            "title": data['title'],
            "body": data['body'],
            "votes": int(0),
            "createdOn": question.createdOn,
            }
            question.add_new_question(new_q)
            return make_response(jsonify({'Message': "Question added successfully", 'Status': 201, "Data": new_q}), 201)
        return make_response(jsonify({'Message': "Meetup with that id not found", 'Status': 404}), 404)


@api.route('/<int:m_id>/questions/<int:qsn_id>')
class SingleQuestion(Resource):
    @api.doc(envelope = 'Question')
    def get(self, m_id, qsn_id):
        '''Get single Question'''
        if meetup.get_single_meetup(m_id):
            a = question.get_single_question(qsn_id)
            if a:
                return a
            return make_response(jsonify({'Message': "Question with that id not found", 'Status': 404}), 404)
        return make_response(jsonify({'Message': "Meetup with that id not found", 'Status': 404}), 404)

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
            return make_response(jsonify({'Message': "Question with that id not found", 'Status': 404}), 404)
        return make_response(jsonify({'Message': "Meetup with that id not found", 'Status': 404}), 404)

@api.route('/questions/<int:qsn_id>/upvote')
class UpVoteQuestion(Resource):
    @api.expect(n_votes, validate = True)
    def patch(self, qsn_id):
        ''' Up votes '''
        item = question.get_single_question(qsn_id)
        if item:
            item['votes'] = item['votes']+ 1
            return make_response(jsonify({'Message': "Vote updated successfully", 'Status': 201, "Data": item}), 201)
        return make_response(jsonify({'Message': "Meetup with that id not found", 'Status': 404}), 404)

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
            return make_response(jsonify({'Message': "Meetup with that id not found", 'Status': 400}), 400)
        return make_response(jsonify({'Message': "Meetup with that id not found", 'Status': 404}), 404)



