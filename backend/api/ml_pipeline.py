import os
import pandas as pd
from flask import Blueprint, request, jsonify
from models.dataset_model import Dataset
from models.ml_model import MLModel
from services.model_training import ModelTrainer
from config.db import db

ml_bp = Blueprint("ml", __name__)

@ml_bp.route("/train", methods=["POST"])
def train_model():
    """Train a machine learning model on a selected dataset"""
    data = request.json
    dataset_id = data.get("dataset_id")
    target_column = data.get("target_column")
    feature_columns = data.get("feature_columns")
    model_type = data.get("model_type", "linear")  # Default to linear regression

    try:
        # Fetch dataset from database
        dataset = Dataset.query.get(dataset_id)
        if not dataset:
            return jsonify({"error": "Dataset not found"}), 404

        # Load dataset into pandas DataFrame
        file_extension = dataset.file_type
        if file_extension == "csv":
            df = pd.read_csv(dataset.file_path)
        elif file_extension == "xlsx":
            df = pd.read_excel(dataset.file_path)
        elif file_extension == "json":
            df = pd.read_json(dataset.file_path)
        else:
            return jsonify({"error": "Unsupported file format"}), 400

        # Ensure target and feature columns exist
        missing_columns = [col for col in [target_column] + feature_columns if col not in df.columns]
        if missing_columns:
            return jsonify({"error": f"Missing columns: {', '.join(missing_columns)}"}), 400

        # Train the model using ModelTrainer
        trainer = ModelTrainer(df, target_column, feature_columns, model_type)
        metrics, feature_importance = trainer.train()

        # Store model metadata in the database
        model = MLModel(
            name=f"{model_type}_model_{dataset_id}",
            dataset_id=dataset_id,
            model_type=model_type,
            parameters={"target": target_column, "features": feature_columns},
            metrics=metrics,
            status="active"
        )
        db.session.add(model)
        db.session.commit()

        return jsonify({
            "message": "Model trained successfully",
            "model_id": model.id,
            "metrics": metrics,
            "feature_importance": feature_importance
        }), 200

    except Exception as e:
        return jsonify({"error": f"Model training failed: {str(e)}"}), 500


@ml_bp.route("/predict", methods=["POST"])
def make_prediction():
    """Make predictions using a trained ML model"""
    data = request.json
    model_id = data.get("model_id")
    input_features = data.get("features")

    try:
        # Fetch trained model from the database
        model = MLModel.query.get(model_id)
        if not model:
            return jsonify({"error": "Model not found"}), 404

        # Load dataset to get feature names
        dataset = Dataset.query.get(model.dataset_id)
        file_extension = dataset.file_type
        if file_extension == "csv":
            df = pd.read_csv(dataset.file_path)
        elif file_extension == "xlsx":
            df = pd.read_excel(dataset.file_path)
        elif file_extension == "json":
            df = pd.read_json(dataset.file_path)
        else:
            return jsonify({"error": "Unsupported file format"}), 400

        # Load the trained model and make predictions
        trainer = ModelTrainer(df, model.parameters["target"], model.parameters["features"], model.model_type)
        predictions = trainer.predict(input_features)

        return jsonify({
            "model_id": model.id,
            "predictions": predictions
        }), 200

    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500
