from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class Membership(db.Model):
  cost = db.Column(db.Double, nullable = False)
  duration = db.Column(db.DateTime, nullable = False)
  is_valid = db.Column(db.Boolean, nullable = False)

  def __init__(self, cost, duration, is_valid):
    self.cost = cost
    self.duration = duration
    self.is_valid = is_valid
    
  def has_membership(self, username, is_valid): 
    if(is_valid):
      #idk what to do here ngl
  
