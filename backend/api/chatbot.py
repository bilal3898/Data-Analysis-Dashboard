from flask import Blueprint, request, jsonify
from models.dataset_model import Dataset
from services.chatbot import DataChatbot
import pandas as pd

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/ask", methods=["POST"])
def ask_chatbot():
    """Handles user queries for dataset insights"""
    data = request.json
    dataset_id = data.get("dataset_id")
    query = data.get("query")

    if not query:
        return jsonify({"error": "Query is required"}), 400

    # Fetch dataset from database
    dataset = Dataset.query.get(dataset_id)
    if not dataset:
        return jsonify({"error": "Dataset not found"}), 404

    df = pd.read_csv(dataset.file_path) if dataset.file_type == "csv" else \
         pd.read_excel(dataset.file_path) if dataset.file_type == "xlsx" else \
         pd.read_json(dataset.file_path)

    # Process query using chatbot
    chatbot = DataChatbot(df)
    response = chatbot.answer_query(query)

    return jsonify({"query": query, "response": response}), 200
