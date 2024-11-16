from flask import Blueprint, jsonify, request
from app.services.user_service import get_all_users, create_user

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify(users), 200

@user_bp.route('/', methods=['POST'])
def add_user():
    data = request.json
    user = create_user(data)
    return jsonify(user), 201
