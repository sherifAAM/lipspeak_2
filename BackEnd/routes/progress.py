from flask import Blueprint, request, jsonify
from models import User
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

progress_blueprint = Blueprint('progress', __name__)

@progress_blueprint.route('/update', methods=['PUT'])
@jwt_required()
def update_progress():
    user_id = get_jwt_identity()
    data = request.get_json()

    user = User.query.get(user_id)
    if user:
        user.lessons_completed = data.get('lessons_completed', user.lessons_completed)
        user.tests_passed = data.get('tests_passed', user.tests_passed)
        user.progress = data.get('progress', user.progress)
        user.current_level = data.get('current_level', user.current_level)
        
        db.session.commit()
        return jsonify({"message": "Progress updated successfully"}), 200

    return jsonify({"message": "User not found"}), 404
