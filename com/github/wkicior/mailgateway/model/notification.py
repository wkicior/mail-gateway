from datetime import datetime

class Rating(object):
    def __init__(self, rating, starting_from):
        self.rating = rating
        self.starting_from = datetime.strptime(starting_from, '%Y-%m-%dT%H:%M:%S.%fZ')

    def __repr__(self):
        return u"Rating: %s; starting_from: %s" % (self.rating, self.starting_from)
        

        
class Notification(object):
    def __init__(self, mail, msg, rating):
        self.mail = mail
        self.msg = msg
        self.rating = rating

    def __repr__(self):
        return u"Notification: mail: %s msg: %s; rating: %s" % (self.mail, self.msg, self.rating)
            
