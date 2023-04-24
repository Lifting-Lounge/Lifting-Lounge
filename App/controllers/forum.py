from App.models import Forum
from App.database import db

def create_message(username, message):
    newMessage = Forum(username=username, message=message)
    try:
        db.session.add(newMessage)
        db.session.commit()
        # print (newMessage.username)
        # newMessage2= Forum.query.filter_by(message_id=1).first()
        # print (newMessage2.username)
        return newMessage
    except:
        return None

def get_all_messages():
    return Forum.query.all()
