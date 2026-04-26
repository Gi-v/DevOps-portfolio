from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS) for all routes
CORS(app)

# A simple in-memory database for our students
students_db = [
    {"id": 1, "name": "Alice Smith", "age": 20, "major": "Engineering"}
]

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify the API is running."""
    return jsonify({
        "status": "healthy",
        "message": "API is up and running!"
    }), 500# changed to 500 for error testing

@app.route('/api/students', methods=['GET'])
def get_all_students():
    """Return all students."""
    return jsonify(students_db), 200

@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Return a single student by ID, or 404 if not found."""
    student = next((s for s in students_db if s["id"] == student_id), None)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404

@app.route('/api/students', methods=['POST'])
def add_student():
    """Add a new student. Requires name, age, and major."""
    data = request.get_json()
    
    # Check if the request has data and all required fields
    if not data or not all(key in data for key in ("name", "age", "major")):
        return jsonify({"error": "Missing required fields"}), 400
        
    new_student = {
        "id": len(students_db) + 1,
        "name": data["name"],
        "age": data["age"],
        "major": data["major"]
    }
    students_db.append(new_student)
    
    return jsonify(new_student), 201

if __name__ == '__main__':
    # Host is set to '0.0.0.0' so it is accessible outside the Docker container
    app.run(host='0.0.0.0', port=5000, debug=True)