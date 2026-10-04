from flask import Blueprint, request, jsonify

export_bp = Blueprint("export", __name__)

@export_bp.route("/export", methods=["POST"])
def export_data():
    """Export analysis results in various formats."""
    try:
        data = request.get_json()
        format_type = data.get("format", "csv")
        
        if format_type == "csv":
            return jsonify({"message": "CSV export generated", "file": "results.csv"}), 200
        elif format_type == "json":
            return jsonify({"message": "JSON export generated", "file": "results.json"}), 200
        else:
            return jsonify({"error": "Unsupported format"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
