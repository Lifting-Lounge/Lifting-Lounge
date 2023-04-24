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

@auth_views.route('/login_page', methods=['GET'])
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
    flash ('Incorrect username or password given!')
    return redirect('/login_page')

@auth_views.route('/logout', methods=['GET'])
def logout_action():
    logout_user()
    return redirect('/home')

@auth_views.route('/signup_page', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@auth_views.route('/signup', methods = ['POST'])
def signup_action():
    data = request.form
    username = data['username']
    password = data['password']
    email = data['email']
    payment = data['payment']
    user = create_user(username, password, email, payment)
    if user:
        login_user(user)
        return redirect('/home')
    else:
        flash ('Username or email already in use!')
        return redirect('/signup_page')
    

