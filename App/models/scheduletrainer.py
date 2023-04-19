from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class ScheduleTrainer(db.Model):
  username = db.Column(db.String(80), nullable = False, db.ForeignKey('user.username')) 
  trainer = db.Column(db.String(120))
  time = db.Column(db.DateTime)
  booked = db.Column(db.Boolean)
