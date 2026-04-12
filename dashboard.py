from flask import Blueprint, request, jsonify
from utils.auth import verify_token

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/data", methods=["GET"])
def get_data():
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"error": "No token"}), 401

    decoded = verify_token(token)

    if not decoded:
        return jsonify({"error": "Invalid token"}), 401

    return jsonify({
        "message": "Welcome to dashboard 🚀",
        "user_id": decoded["user_id"]
    })
