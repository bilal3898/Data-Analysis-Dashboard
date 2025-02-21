from transformers import pipeline
import pandas as pd
from services.insight_generator import InsightGenerator
from services.anomaly_detection import AnomalyDetector

class DataChatbot:
    """AI-powered chatbot for answering dataset-related questions"""

    def __init__(self, df):
        self.df = df
        self.qa_pipeline = pipeline("text-generation", model="facebook/blenderbot-400M-distill")

    def get_basic_stats(self):
        """Returns basic statistics of the dataset"""
        return self.df.describe().to_string()

    def get_insights(self):
        """Generates AI-powered insights using InsightGenerator"""
        insight_gen = InsightGenerator(self.df)
        return insight_gen.get_all_insights()

    def get_anomalies(self):
        """Detects anomalies in the dataset using AnomalyDetector"""
        anomaly_detector = AnomalyDetector(self.df)
        return anomaly_detector.get_all_anomalies()

    def answer_query(self, query):
        """Processes user queries and generates AI-powered responses"""
        query = query.lower()

        if "summary" in query or "describe" in query:
            return self.get_basic_stats()
        elif "insight" in query or "trend" in query:
            return "\n".join(self.get_insights())
        elif "anomaly" in query or "outlier" in query:
            return str(self.get_anomalies())
        else:
            # AI-generated response for general queries
            response = self.qa_pipeline(query, max_length=100, do_sample=True)
            return response[0]['generated_text']
