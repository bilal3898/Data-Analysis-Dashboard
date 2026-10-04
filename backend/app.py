from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
from config.config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Force SQLite for now
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dashboard.db'

# Enable CORS for handling cross-origin requests
CORS(app, supports_credentials=True)

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize JWT authentication
jwt = JWTManager(app)

# Import models to register them with SQLAlchemy
from models.user_model import User
from models.dataset_model import Dataset
from models.ml_model import MLModel

# Import and register blueprints
from api.upload import upload_bp
from api.train import train_bp
from api.predict import predict_bp
from api.analyze import analyze_bp
from api.export import export_bp
from api.status import status_bp

app.register_blueprint(upload_bp, url_prefix='/api')
app.register_blueprint(train_bp, url_prefix='/api')
app.register_blueprint(predict_bp, url_prefix='/api')
app.register_blueprint(analyze_bp, url_prefix='/api')
app.register_blueprint(export_bp, url_prefix='/api')
app.register_blueprint(status_bp, url_prefix='/api')

# Add datasets endpoint directly here
@app.route("/api/datasets", methods=["GET"])
def get_datasets():
    datasets = [
        {"id": 1, "name": "Sales Data"},
        {"id": 2, "name": "Customer Data"},
        {"id": 3, "name": "Marketing Data"}
    ]
    return jsonify(datasets)

# Add a root route to prevent "404 Not Found"
@app.route("/")
def home():
    return jsonify({"message": "AI Dashboard Backend is Running!"})

# Create database tables
with app.app_context():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
