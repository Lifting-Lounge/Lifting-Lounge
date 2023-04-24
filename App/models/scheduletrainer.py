from App.database import db 
from werkzeug.security import generate_password_hash, check_password_hash

class ScheduleTrainer(db.Model):
  user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
  trainer_id = db.Column(db.Integer, primary_key = True)
  trainer = db.Column(db.String(120))
  time = db.Column(db.DateTime)
  booked = db.Column(db.Boolean)

def __init__(self,username, trainer, time, booked):
    self.username = username
    self.trainer= trainer
    self.time = time
    self.booked =booked
    
def book_appt(trainer, booked): 
  if(booked == False): 
    booked = True
    #idk here either sorry
