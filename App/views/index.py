from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import (create_user, get_all_exercises, load_api_muscle)

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/home', methods=['GET'])        #loads biceps as default
def index_page():
    muscle = "biceps"
    exercises = load_api_muscle(muscle)
    
    return render_template('index.html', exercises=exercises)


@index_views.route('/', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass', 'bob@mail.com', 'cash')
    return redirect('/home')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})