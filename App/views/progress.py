from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify

progress_views = Blueprint('progress_views', __name__, template_folder='../templates')

@progress_views.route('/progress', methods=['GET'])
def profile_page():
    return render_template('progress.html')