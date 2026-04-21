from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS) for all routes
CORS(app)

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify the API is running."""
    return jsonify({
        "status": "healthy",
        "message": "API is up and running!"
    }), 200

if __name__ == '__main__':
    # Host is set to '0.0.0.0' so it is accessible outside the Docker container
    app.run(host='0.0.0.0', port=5000, debug=True)