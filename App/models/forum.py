from App.database import db

class Forum(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable = False)
    message = db.Column(db.String(240), nullable = False)

    def __init__(self, username, message):
        self.username = username
        self.message = message

    def toJSON(self):
        return{
            'username': self.username,
            'message': self.message,
        }


