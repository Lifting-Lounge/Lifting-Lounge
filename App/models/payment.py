from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class Payment(db.Model):
  payment_id = db.Column(db.Integer, primary_key=True)
  payment_method = db.Column(db.String(120), db.ForeignKey('user.payment_info'))
  amount_paid = db.Column(db.Double)
  expires = db.Column(db.DateTime, nullable = False)
  
  
  def __init__(self, payment_method, amount_paid, expires):
    self.payment_method = payment_method
    self.amount_paid = amount_paid
    self.expires = expires
    
   
