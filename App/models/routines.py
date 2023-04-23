from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class Routines(db.Model):
  routine_id = db.Column(db.Integer, primary_key= True)
  workout_name = db.Column(db.String(120), nullable = False)
  reps = db.Column(db.Integer) 
  sets = db.Column(db.Integer) 
  routine_name = db.Column(db.String(120))
  day = db.Column(db.String(120)) 
  
  def __init__(self, workout_name, reps, sets, routine_name, day):
    self.workout_name = workout_name
    self.reps = reps
    self.sets = sets
    self.routine_name = routine_name
    self.day = day
    
  def get_json(self): 
    return{
      "workout_name": workout_name,
      "reps": reps,
      "sets": sets,
      "routine_name": routine_name,
      "day": day
    }
