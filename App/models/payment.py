from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class Payment(db.Model):
  payment_method = db.Column(db.String, nullable = False)
  amount_paid = db.Column(db.Double)
  expires = db.Column(db.DateTime, nullable = False)
  
