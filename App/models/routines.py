from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class Routines(db.Model):
  workout_name = db.Column(db.String(120), nullable = False)
  reps = db.Column(db.Integer) 
  sets = db.Column(db.Integer) 
  routine_name = db.Column(db.String(120))
  day = db.Column(db.String(120)) 
  
