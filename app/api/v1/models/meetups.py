from datetime import datetime

class Meetups:
    """ Meetups constructor """
    def __init__(self, m_id, location, images, topic, happeningOn):
        self.m_id = m_id
        self.createdOn = datetime.now()
        self.location = location
        self.images = images
        self.topic = topic
        self.happeningOn = happeningOn
        self.Meetups = []

    """ Method for getting a single meetup """
    def get_single_meetup(self, m_id):
        for m in self.Meetups:
            if m['m_id'] == m_id:
                return m