from flask import Blueprint, request, jsonify

analyze_bp = Blueprint('analyze', __name__)

@analyze_bp.route('/analyze', methods=['POST'])
def analyze_data():
    """Endpoint to analyze uploaded data."""
    try:
        data = request.get_json()
        if not data or not isinstance(data, list):
            return jsonify({"error": "Invalid input, expected a list of numbers"}), 400

        try:
            numeric_data = [float(x) for x in data]
        except ValueError:
            return jsonify({"error": "List must contain only numbers"}), 400

        analysis_result = {
            "total_records": len(numeric_data),
            "mean_value": sum(numeric_data) / len(numeric_data) if numeric_data else 0
        }

        return jsonify({"message": "Analysis complete", "result": analysis_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
