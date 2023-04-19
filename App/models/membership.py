from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class Membership(db.Model):
  cost = db.Column(db.Double, nullable = False)
  duration = db.Column(db.DateTime, nullable = False)
  restrictions = db.COlumn(db.String(120))
