from flask import Blueprint, redirect, render_template, request, flash, send_from_directory, jsonify
from flask_login import current_user
from App.controllers import (get_all_messages, create_message)

forum_views = Blueprint('forum_views', __name__, template_folder='../templates')

@forum_views.route('/forum', methods=['GET'])
def profile_page():
    message = get_all_messages()
    return render_template('forum.html', message=message)

@forum_views.route('/add_forum', methods = ['POST'])
def add_to_form():
    data = request.form
    message = data['message']
    username = current_user.username
    new_message = create_message(username, message)
    
    if new_message:
        return redirect('/forum')
    flash('Error in adding new message to forum!')
    return redirect('/forum')