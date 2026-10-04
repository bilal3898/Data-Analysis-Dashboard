from flask import Blueprint, request, jsonify
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

train_bp = Blueprint("train", __name__)

@train_bp.route("/train", methods=["POST"])
def train_model():
    """Train a simple machine learning model and return accuracy."""
    try:
        data = request.get_json()
        if "X" not in data or "y" not in data:
            return jsonify({"error": "Missing 'X' or 'y' in request data"}), 400

        X = pd.DataFrame(data["X"])
        y = pd.Series(data["y"])

        model = LinearRegression()
        model.fit(X, y)

        joblib.dump(model, "model.pkl")

        return jsonify({"message": "Model trained successfully", "score": model.score(X, y)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
