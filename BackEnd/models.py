from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    current_level = db.Column(db.String(50), default="Beginner")
    lessons_completed = db.Column(db.Integer, default=0)
    tests_passed = db.Column(db.Integer, default=0)
    progress = db.Column(db.Float, default=0.0)  # Percentage

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(50), nullable=False)
    lesson_number = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    is_test = db.Column(db.Boolean, default=False)
