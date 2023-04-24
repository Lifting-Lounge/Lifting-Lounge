from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import (get_all_messages)

forum_views = Blueprint('forum_views', __name__, template_folder='../templates')

@forum_views.route('/forum', methods=['GET'])
def profile_page():
    # message = get_all_messages()
    return render_template('forum.html')