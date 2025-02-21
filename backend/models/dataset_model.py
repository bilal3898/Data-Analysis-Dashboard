from datetime import datetime
from config.db import db

class Dataset(db.Model):
    """Database model for storing dataset metadata"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    file_type = db.Column(db.String(50), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    columns = db.Column(db.JSON)  # Stores column names in JSON format
    row_count = db.Column(db.Integer)
    processed = db.Column(db.Boolean, default=False)  # Indicates if dataset has been processed
