import pandas as pd
from flask import Blueprint, request, jsonify
from models.dataset_model import Dataset
from services.insight_generator import InsightGenerator
from services.anomaly_detection import AnomalyDetector

insights_bp = Blueprint("insights", __name__)

@insights_bp.route("/generate", methods=["POST"])
def generate_insights():
    """Generate AI-powered insights and detect anomalies for a dataset"""
    data = request.json
    dataset_id = data.get("dataset_id")

    try:
        # Validate input
        if not dataset_id:
            return jsonify({"error": "Dataset ID is required"}), 400

        # Fetch dataset from the database
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

        # Ensure dataset is not empty
        if df.empty:
            return jsonify({"error": "Dataset is empty"}), 400

        # Generate insights
        insight_generator = InsightGenerator(df)
        insights = insight_generator.get_all_insights()

        # Detect anomalies
        anomaly_detector = AnomalyDetector(df)
        anomalies = anomaly_detector.get_all_anomalies()

        return jsonify({
            "message": "Insights and anomalies generated successfully",
            "dataset_id": dataset_id,
            "insights": insights,
            "anomalies": anomalies
        }), 200

    except FileNotFoundError:
        return jsonify({"error": "Dataset file not found"}), 404
    except pd.errors.ParserError:
        return jsonify({"error": "Error parsing dataset file"}), 400
    except Exception as e:
        return jsonify({"error": f"Failed to generate insights: {str(e)}"}), 500
