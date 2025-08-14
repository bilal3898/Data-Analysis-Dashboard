from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
from config.config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)  # Load configurations from Config class

# Enable CORS for handling cross-origin requests
CORS(app)

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize JWT authentication
jwt = JWTManager(app)

# Import models to register them with SQLAlchemy
from models.user_model import User
from models.dataset_model import Dataset
from models.ml_model import MLModel

# Import and register blueprints (comment out for now since the files might not exist)
# from api.upload import upload_bp
# from api.train import train_bp
# from api.predict import predict_bp
# from api.analyze import analyze_bp
# from api.export import export_bp

# app.register_blueprint(upload_bp, url_prefix='/api')
# app.register_blueprint(train_bp, url_prefix='/api')
# app.register_blueprint(predict_bp, url_prefix='/api')
# app.register_blueprint(analyze_bp, url_prefix='/api')
# app.register_blueprint(export_bp, url_prefix='/api')

# Create database tables
with app.app_context():
    db.create_all()

# Basic route for testing
@app.route('/')
def hello():
    return {"message": "Smart Data Analysis Dashboard API is running!"}

@app.route('/api/health')
def health():
    return {"status": "healthy", "message": "Backend is running successfully"}

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
