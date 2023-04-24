from flask import Blueprint, redirect, render_template, request, flash, send_from_directory, jsonify
from flask_login import current_user
from App.controllers import (create_exercise, get_all_exercises, load_api_muscle)
from App.models import Exercises

exercise_views = Blueprint('exercise_views', __name__, template_folder='../templates')

@exercise_views.route('/exercises', methods=['GET','POST'])
def muscle_action():
    muscle = str(request.form)  
    exercises = load_api_muscle(muscle)
    
    return render_template('index.html', exercises=exercises)
    
