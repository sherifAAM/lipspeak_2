from flask import Blueprint, jsonify
from models import Lesson

lessons_blueprint = Blueprint('lessons', __name__)

@lessons_blueprint.route('/<level>', methods=['GET'])
def get_lessons(level):
    lessons = Lesson.query.filter_by(level=level).all()
    return jsonify([{
        "id": lesson.id,
        "lesson_number": lesson.lesson_number,
        "content": lesson.content,
        "is_test": lesson.is_test
    } for lesson in lessons]), 200

@lessons_blueprint.route('/<level>/<lesson_number>', methods=['GET'])
def get_lesson(level, lesson_number):
    lesson = Lesson.query.filter_by(level=level, lesson_number=lesson_number).first()
    if lesson:
        return jsonify({
            "id": lesson.id,
            "lesson_number": lesson.lesson_number,
            "content": lesson.content,
            "is_test": lesson.is_test
        }), 200

    return jsonify({"message": "Lesson not found"}), 404
