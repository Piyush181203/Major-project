from flask import Blueprint, request, jsonify
from models import create_user, get_user
from utils.auth import generate_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    try:
        create_user(data["username"], data["password"])
        return jsonify({"msg": "User registered"})
    except:
        return jsonify({"error": "User exists"}), 400

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = get_user(data["username"], data["password"])

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    token = generate_token(user["id"])
    return jsonify({"token": token})
