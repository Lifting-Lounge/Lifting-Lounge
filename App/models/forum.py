from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
db = SQLAlchemy()

class Forum(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable = False)
    message = db.Column(db.String(240), nullable = False)

    
