from datetime import datetime

Questions = []

class Question:
    """ Questions constructor """
    def __init__(self, title=None, body=None, votes=None):
        self.createdOn = datetime.now()
        self.title = title
        self.body = body
        self.votes = 0

    def add_new_question(self, new_q):

        new_qsn ={
        "qsn_id": new_q['qsn_id'],
        "meetup_id": new_q['meetup_id'],
        "title": new_q['title'],
        "body": new_q['body'],
        "votes": new_q['votes'],
        "createdOn": str(datetime.now()),
        }

        Questions.append(new_qsn)

    """ Method for getting single question """
    def get_single_question(self, qsn_id):
        for q in Questions:
            if q['qsn_id'] == qsn_id:
                return q