from datetime import datetime

Responses = [] 

class Responds:
    """ Respond constructor """

    def __init__(self, r_id=None, status=None):
        self.r_id = r_id
        self.status = status

    def add_new_response(self, res):
        res ={
            "r_id": res['r_id'],
            "meetup_id": res['meetup_id'],
            "topic": res['topic'],
            "status": res['status']  
            }
        Responses.append(res) 