from flask import Blueprint, redirect, render_template, request, flash, send_from_directory, jsonify
from flask_login import current_user
from App.controllers import (get_all_exercises, load_api_muscle)

from.index import index_views
from.exercise import exercise_views

exercise_views = Blueprint('exercise_views', __name__, template_folder='../templates')

@exercise_views.route('/exercises/<muscle>', methods=['GET'])
def muscle_page():
    data = request.form
    muscle = data['muscle']
    exercises = load_api_muscle(muscle)
    if exercises:
        return render_template('index.html', exercises=exercises)
    flash ("Muscle not found!")
    return redirect('/')
