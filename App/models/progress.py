from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class Progress(db.Model):
  height = db.Column(db.Integer)
  weight = db.Column(db.Integer)
  exercises = db.Column(db.String(120)) 
  goals = db.Column(db.String(120))
  routine = db.Column(db.String(120)) 
