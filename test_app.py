import pytest
from app import app

# Create a test client fixture to be used in all tests
@pytest.fixture
def client():
    # Configure the app for testing
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Test the health check endpoint returns 200 OK and expected JSON."""
    response = client.get('/api/health')
    
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert data["message"] == "API is up and running!"

def test_get_all_students(client):
    """Test retrieving all students returns a 200 OK."""
    response = client.get('/api/students')
    
    assert response.status_code == 200
    data = response.get_json()
    # Assuming your API returns a list of students
    assert isinstance(data, list)

def test_get_non_existent_student(client):
    """Test retrieving a student that doesn't exist returns a 404."""
    # Using an ID that is highly unlikely to exist
    response = client.get('/api/students/99999')
    
    assert response.status_code == 404

def test_add_valid_student(client):
    """Test adding a valid student returns a 201 and the correct name."""
    new_student = {
        "name": "Jane Doe",
        "age": 22,
        "major": "Computer Science"
    }
    
    response = client.post('/api/students', json=new_student)
    
    assert response.status_code == 201
    data = response.get_json()
    # Check that the API responds with the data we sent, specifically the name
    assert "name" in data
    assert data["name"] == "Jane Doe"

def test_add_student_missing_field(client):
    """Test adding a student with missing required fields returns a 400."""
    # Missing the 'name' field
    incomplete_student = {
        "age": 22,
        "major": "Computer Science"
    }
    
    response = client.post('/api/students', json=incomplete_student)
    
    assert response.status_code == 400