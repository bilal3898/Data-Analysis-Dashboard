from flask import Blueprint, jsonify

status_bp = Blueprint("status", __name__)

@status_bp.route("/status", methods=["GET"])
def status():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "message": "Backend is running"}), 200
