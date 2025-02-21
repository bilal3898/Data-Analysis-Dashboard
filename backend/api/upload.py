import os
import pandas as pd
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from models.dataset_model import Dataset
from config.db import db
from app import app
from services.data_cleaning import clean_dataset  # Import the cleaning function

upload_bp = Blueprint("upload", __name__)

# Allowed file extensions
ALLOWED_EXTENSIONS = {"csv", "xlsx", "json"}

def allowed_file(filename):
    """Check if the uploaded file has a valid extension"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_bp.route("/upload", methods=["POST"])
def upload_file():
    """Handle file uploads and save cleaned dataset details in the database"""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        try:
            # Secure the filename
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

            # Save the file to the uploads folder
            file.save(filepath)

            # Load dataset
            if filename.endswith(".csv"):
                df = pd.read_csv(filepath)
            elif filename.endswith(".xlsx"):
                df = pd.read_excel(filepath)
            elif filename.endswith(".json"):
                df = pd.read_json(filepath)
            else:
                return jsonify({"error": "Unsupported file format"}), 400

            # Clean the dataset
            df = clean_dataset(df)

            # Save the cleaned dataset back to file
            cleaned_filepath = os.path.join(app.config["UPLOAD_FOLDER"], f"cleaned_{filename}")
            df.to_csv(cleaned_filepath, index=False) if filename.endswith(".csv") else \
                df.to_excel(cleaned_filepath, index=False) if filename.endswith(".xlsx") else \
                df.to_json(cleaned_filepath, orient="records")

            # Create dataset record in the database
            dataset = Dataset(
                name=filename,
                file_path=cleaned_filepath,  # Store the cleaned file path
                file_type=filename.rsplit(".", 1)[1].lower(),
                processed=True  # Mark as processed
            )

            db.session.add(dataset)
            db.session.commit()

            return jsonify({
                "message": "File uploaded and cleaned successfully",
                "dataset_id": dataset.id,
                "file_name": dataset.name,
                "file_path": dataset.file_path
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Invalid file type"}), 400
