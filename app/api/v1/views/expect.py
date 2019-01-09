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