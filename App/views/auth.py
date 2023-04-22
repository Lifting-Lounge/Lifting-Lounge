from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_login import login_required, login_user, current_user, logout_user

from.index import index_views

from App.controllers import (
    create_user,
    login 
)

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')

'''
Page/Action Routes
'''

@auth_views.route('/', methods=['GET'])
def login_page():
    return render_template('login.html')

@auth_views.route('/login', methods = ['POST'])
def login_action():
    data = request.form
    username = data['username']
    password = data['password']
    user = login(username, password)
    if user:
        login_user(user)
        return redirect('/home')
    return 'bad username or password given', 401

@auth_views.route('/logout', methods=['GET'])
def logout_page():
    data = request.form
    user = login(data['username'], data['password'])
    return 'logged out!'

