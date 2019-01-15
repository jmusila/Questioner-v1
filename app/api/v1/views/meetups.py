#Third party imports
from flask_restplus import Resource
from flask import request, make_response, jsonify

#Local imports
from app.api.v1.models.meetups import Meetup, Meetups
from app.api.v1.views.expect import MeetupsModel

meetup = Meetup()
new_meetup = MeetupsModel().meetups
api = MeetupsModel().api

@api.route('')
class MeetupOp(Resource):
    @api.doc('list_meetups')
    def get(self):
        '''List all meetups'''
        return make_response(jsonify({"Status": 200, "Meetups":Meetups}), 200)

    @api.expect(new_meetup, validate = True)
    def post(self):
        '''Post a meetup'''
        data = request.get_json()
        mtup ={
            "m_id": int(len(Meetups)+ 1),
            "location": data['location'],
            "images": data['images'],
            "topic": data['topic'],
            "happeningOn": data['happeningOn'], 
            "createdOn": meetup.createdOn  
        }
        meetup.create_meetup(mtup)
        return make_response(jsonify({'Message': "Meetup added successfully", 'Status': 201, "data":mtup}), 201)


@api.route('/<int:m_id>')
class AlterMeetup(Resource):
    @api.doc(envelope = 'Meetup')
    def get(self, m_id):
        '''Get single Meetup'''
        a = meetup.get_single_meetup(m_id)
        if a:
            return a
        return {'Message': "Meetup with that Id not found", 'Status': 404}, 404

    def delete(self, m_id):
        '''Delete Meetup'''
        d = meetup.get_single_meetup(m_id)
        if d:
            Meetups.remove(d)
            return {"Message": "Meetup deleted successfully", 'Status': 200}, 200
        return make_response(jsonify({'Message': "Meetup with that Id not found", 'Status': 404}), 404)

    @api.expect(new_meetup, validate = True)
    def put(self, m_id):
        '''Update Meetup'''
        u = api.payload
        d = meetup.get_single_meetup(m_id)
        if d:
            u['m_id'] = d['m_id']
            d.update(u)
            return make_response(jsonify({'Message': "Meetup updated successfully", 'Status': 201, "Data":d}), 201)
        return make_response(jsonify({'Message': "Meetup with that Id not found", 'Status': 404}), 404)