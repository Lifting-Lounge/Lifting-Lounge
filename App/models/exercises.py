from App.database import db

class Exercises(db.Model):
    name = db.Column(db.String(120),primary_key = True, nullable = False)
    type = db.Column(db.String(120), nullable = False)
    muscle = db.Column(db.String(120), nullable = False)
    equipment = db.Column(db.String(120), nullable = False)
    difficulty = db.Column(db.String(120), nullable = False)
    instructions = db.Column(db.String(120), nullable = False)

    def toJSON(self):
        return {
            'name': self.name,
            'type': self.type,
            'muscle': self.muscle,
            'equipment': self.equipment,
            'difficulty': self.difficulty,
            'instructions': self.instructions
        }