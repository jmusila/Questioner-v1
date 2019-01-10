from datetime import datetime

class Question:
    """ Questions constructor """
    def __init__(self, qsn_id, meetup_id, title, body, votes):
        self.qsn_id = qsn_id
        self.createdOn = datetime.now()
        self.meetup_id = meetup_id
        self.title = title
        self.body = body
        self.votes = votes
        self.Questions = []

    """ Method for getting single question """
    def get_single_question(self, qsn_id):
        for q in self.Questions:
            if q['qsn_id'] == qsn_id:
                return q