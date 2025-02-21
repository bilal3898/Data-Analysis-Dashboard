from datetime import datetime
from config.db import db

class MLModel(db.Model):
    """Database model for storing trained machine learning models"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)  # Model name
    dataset_id = db.Column(db.Integer, db.ForeignKey('dataset.id'), nullable=False)  # Link to dataset
    model_type = db.Column(db.String(50), nullable=False)  # Model type (e.g., linear regression, random forest)
    parameters = db.Column(db.JSON, nullable=True)  # Stores model hyperparameters
    metrics = db.Column(db.JSON, nullable=True)  # Stores evaluation metrics (accuracy, MSE, etc.)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp when the model was created
    status = db.Column(db.String(50), default="active")  # Status (e.g., active, deprecated)
    
    # Relationship with Dataset
    dataset = db.relationship("Dataset", backref=db.backref("models", lazy=True))
