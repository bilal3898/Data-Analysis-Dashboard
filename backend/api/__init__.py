from flask import Blueprint

# Import API modules
from api.upload import upload_bp
from api.ml_pipeline import ml_bp
from api.insights import insights_bp
from api.advanced_ml import advanced_ml_bp
from api.auth import auth_bp

# Create a main Blueprint
api_bp = Blueprint("api", __name__)

# Register API routes
api_bp.register_blueprint(upload_bp, url_prefix="/api")
api_bp.register_blueprint(ml_bp, url_prefix="/api/ml")
api_bp.register_blueprint(insights_bp, url_prefix="/api/insights")
api_bp.register_blueprint(advanced_ml_bp, url_prefix="/api/advanced-ml")
api_bp.register_blueprint(auth_bp, url_prefix="/api/auth")

# Function to initialize API
def init_api(app):
    """Attach all API blueprints to the Flask app"""
    app.register_blueprint(api_bp)
