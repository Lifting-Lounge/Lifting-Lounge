from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class ScheduleTrainer(db.Model):
  username = db.Column(db.String(80), nullable = False, db.ForeignKey('user.username')) 
  trainer = db.Column(db.String(120))
  time = db.Column(db.DateTime)
  booked = db.Column(db.Boolean)

def __init__(self,username, trainer, time, booked):
    self.username = username
    self.trainer= trainer
    self.time = time
    self.booked =booked
    
def book_appt(trainer, booked): 
  if(!booked): 
    booked = True
    #idk here either sorry
