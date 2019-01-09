""" This file contains the models expected for the API """

#Third party imports 
from flask_restplus import fields, Namespace 

class MeetupsModel:
    """
    Meetup input data

    """
    api = Namespace('Meetups', description = 'Meetups Routes')
    meetups = api.model('Meetup', {
        'm_id':fields.Integer(required=True, description='The unique identifier of the meetup'),
        'createdOn': fields.String(required=True, description='This time the meetup was created'),
        'location': fields.String(required=True, description='The meetup location'),
        'images': fields.String(required=True, description='The images attached to a meetup'),
        'topic': fields.String(required=True, description='The meetup topic'),
        'happeningOn': fields.String(required=True, description='The date the meetup is happening'),
    })

class QuestionModel:
    """
    Question input data

    """
    api = Namespace('Questions', description='Questions Routes')
    questions = api.model('Question', {
        'qsn_id':fields.Integer(required=True, description='The unique identifier of the question'),
        'body': fields.String(required=True, description='The body of the question'),
        'meetup_id': fields.Integer(required=True, description='The meetup unique identifier'),
        'createdOn': fields.String(required=True, description='The time the question was posted'),
        'title': fields.String(required=True, description='The title of the question'),
        'votes': fields.String(required=True, description='The number of votes a question contains'),
    })

class ResponseModel:
    """
    Response input data

    """
    api = Namespace('Responds', description = 'Responses Routes')
    responses = api.model('Response', {
        'r_id':fields.Integer(required=True, description='The unique identifier of the comment'),
        'meetup_id': fields.String(required=True, description='Meetup unique identifier'),
        'topic': fields.String(required=True, description='The topic of the meetup'),
        'status': fields.String(required=True, description='The response status'),
    })