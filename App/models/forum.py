from App.database import db

class Forum(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable = False)
    message = db.Column(db.String(240), nullable = False)

    def __init__(self, message_id, username, message):
        self.ownerId = message_id
        self.username = username
        self.message = message

    def toJSON(self):
        return{
            'message_id': self.message_id,
            'username': self.username,
            'message': self.message,
        }


