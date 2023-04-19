from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class Equipment(db.Model):
  category = db.Column(db.String(120), nullable = False)
  name = db.Column(db.String(120), unique = True, nullable = False)
  has_exercises = db.Column(db.Boolean, nullable= False)
