from flask import Blueprint, request, jsonify
import joblib

predict_bp = Blueprint("predict", __name__)

@predict_bp.route("/predict", methods=["POST"])
def predict():
    """Make predictions using a trained model."""
    try:
        data = request.get_json()
        if "input_data" not in data:
            return jsonify({"error": "Missing input_data"}), 400

        model = joblib.load("model.pkl")
        prediction = model.predict([data["input_data"]])

        return jsonify({"prediction": prediction.tolist()}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
