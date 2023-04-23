from App.models import Exercises
from App.database import db
from App.config import config
import requests
import json

def create_exercise(name, type, muscle, equiptment, difficulty, instructions):
    newExercise = Exercises (name = name, type = type, equipment = equipment, difficulty = difficulty, instructions = instructions)
    db.session.add (newExercise)
    db.session.commit
    return newExercise

def get_exercise(name):
    exercise = Exercises.query.filter_by(name = name).first
    if (exercise):
        return exercise
    return None

def get_all_exercises ():
    return Exercises.query.all()

def load_api_muscle (muscle):
    api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
    response = requests.get(api_url, headers={'X-Api-Key': 'vJxo3r4nHGTiSprXx+0Jdg==ckMfjuOP0gRZAi5Q'})
    if response.status_code == requests.codes.ok:
        return json.loads(response.text)
    else:
        print("Error:", response.status_code, response.text)

def cache_api_exercises():
    exercises_json = load_api_muscle(biceps)
    exercises_list = []
    for exercises in exercises_json:
        new_exercise = Exercises(name=exercises['name'], type = exercises['type'], equipment=exercises['equipment'], difficulty=exercises['difficulty'], instructions = exercises['instructions'])
        exercises_list.append(new_exercise)
        db.session.add(new_exercise)
    db.session.commit()
    return exercises_list