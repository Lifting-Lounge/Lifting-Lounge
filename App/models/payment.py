from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class Payment(db.Model):
  
