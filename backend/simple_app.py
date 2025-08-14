from flask import Flask
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for handling cross-origin requests
CORS(app)

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