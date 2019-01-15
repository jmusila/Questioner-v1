from datetime import datetime

Meetups = []
class Meetup:
    """ Meetups constructor """
    def __init__(self, m_id=None, location=None, images=None, topic=None, happeningOn=None):
        self.m_id = m_id
        self.createdOn = datetime.now()
        self.location = location
        self.images = images
        self.topic = topic
        self.happeningOn = happeningOn

    def create_meetup(self, mtup):
        meetup = {
            "m_id": mtup['m_id'],
            "location": mtup['location'],
            "images": mtup['images'],
            "topic": mtup['topic'],
            "happeningOn": mtup['happeningOn'], 
            "createdOn": str(datetime.now()) 
        }
        Meetups.append(meetup)

    """ Method for getting a single meetup """
    def get_single_meetup(self, m_id):
        for m in Meetups:
            if m['m_id'] == m_id:
                return m