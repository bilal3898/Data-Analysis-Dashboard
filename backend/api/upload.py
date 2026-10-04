import os
import pandas as pd
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from models.dataset_model import Dataset
from config.db import db
from services.data_cleaning import clean_dataset

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
            filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)

            # Save the file to the uploads folder
            file.save(filepath)
            print(f"File saved to: {filepath}")

            # Load dataset
            try:
                if filename.endswith(".csv"):
                    df = pd.read_csv(filepath)
                elif filename.endswith(".xlsx"):
                    df = pd.read_excel(filepath)
                elif filename.endswith(".json"):
                    df = pd.read_json(filepath)
                else:
                    return jsonify({"error": "Unsupported file format"}), 400
                print(f"Dataset loaded with {len(df)} rows")
            except Exception as e:
                print(f"Error loading file: {str(e)}")
                return jsonify({"error": f"Error loading file: {str(e)}"}), 400

            # Clean the dataset with error handling
            try:
                original_rows = len(df)
                df = clean_dataset(df)
                print(f"Dataset cleaned: {original_rows} -> {len(df)} rows")
            except Exception as e:
                print(f"Error cleaning dataset: {str(e)}")
                print("Continuing with original data")

            # Save the cleaned dataset back to file
            cleaned_filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], f"cleaned_{filename}")
            try:
                if filename.endswith(".csv"):
                    df.to_csv(cleaned_filepath, index=False)
                elif filename.endswith(".xlsx"):
                    df.to_excel(cleaned_filepath, index=False)
                else:
                    df.to_json(cleaned_filepath, orient="records")
                print(f"Cleaned file saved to: {cleaned_filepath}")
            except Exception as e:
                print(f"Error saving cleaned file: {str(e)}")
                return jsonify({"error": f"Error saving cleaned file: {str(e)}"}), 500

            # Create dataset record in the database
            try:
                dataset = Dataset(
                    name=filename,
                    file_path=cleaned_filepath,
                    file_type=filename.rsplit(".", 1)[1].lower(),
                    columns=list(df.columns),
                    row_count=len(df),
                    processed=True
                )

                db.session.add(dataset)
                db.session.commit()
                print(f"Dataset saved to database with ID: {dataset.id}")
            except Exception as e:
                print(f"Error saving to database: {str(e)}")
                db.session.rollback()
                return jsonify({"error": f"Error saving to database: {str(e)}"}), 500

            return jsonify({
                "message": "File uploaded and cleaned successfully",
                "dataset_id": dataset.id,
                "file_name": dataset.name,
                "file_path": dataset.file_path,
                "row_count": dataset.row_count,
                "columns": dataset.columns
            }), 200

        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            import traceback
            traceback.print_exc()
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Invalid file type"}), 400
