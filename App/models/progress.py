from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class Progress(db.Model):
  progress_id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey(user.id))
  height = db.Column(db.Integer)
  weight = db.Column(db.Integer)
  exercises = db.Column(db.String(120)) 
  goals = db.Column(db.String(120))
  routine = db.Column(db.String(120)) 
  
  def __init__(self, height, weight,exercises, goals, routine): 
    self.height = height
    self.weight = weight
    self.exercises= exercises
    self.goals = goals
    self.routine = routine
    
  
  def get_json(self):
    return{
      'height': height
      'weight': weight
      'exercises': exercises
      'goals': goals
      'routine': routine
    }
  
  # def new_measurements(): 
    
