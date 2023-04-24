from App.models import Forum
from App.database import db

def create_message(username, message):
    newMessage = Forum (username=username, message=message)
    try:
        db.session.add(newMessage)
        db.session.commit
        return newMessage
    except:
        return None

def get_all_messages():
    return Forum.query.all()
