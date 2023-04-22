from flask_login import login_user, login_manager, logout_user, LoginManager
from App.models import *


def login(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        login_user(user)
        return user
    return None

def setup_flask_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    return login_manager

