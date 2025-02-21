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

# Import and register blueprints
from backend.api.upload import upload_bp
from backend.api.train import train_bp
from backend.api.predict import predict_bp
from backend.api.analyze import analyze_bp
from backend.api.export import export_bp

app.register_blueprint(upload_bp, url_prefix='/api')
app.register_blueprint(train_bp, url_prefix='/api')
app.register_blueprint(predict_bp, url_prefix='/api')
app.register_blueprint(analyze_bp, url_prefix='/api')
app.register_blueprint(export_bp, url_prefix='/api')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
