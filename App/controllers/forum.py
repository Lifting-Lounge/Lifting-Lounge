from App.models import Forum
from App.database import db
from App.config import config
import requests
import json

def create_message(username, message):
    newMessage = Forum (username=username, message=message)
    db.session.add(newMessage)
    db.session.commit
    return newMessage

def get_all_messages():
    return Forum.query.all()
