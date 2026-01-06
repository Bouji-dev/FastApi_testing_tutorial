from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World'}

def test_get_ping():
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}

def test_hello_with_name():
    response = client.get('/hello?name=Ehsan')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello Ehsan'}

def test_hello_without_name():
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello Anonymous'}

def test_create_user_success():
    payload = {
        'username': 'Ehsan',
        'age': 30
    }
    response = client.post('/users', json=payload)

    assert response.status_code == 200
    assert response.json() == payload

def test_create_user_validation_error():
    payload = {
        'age': 30
    }
    response = client.post('/users', json=payload)

    assert response.status_code == 422

def test_check_age_allowed():
    response = client.post('/check-age', json={'age': 20})

    assert response.status_code == 200
    assert response.json() == {'status': 'allowed'}

def test_check_age_not_allowed():
    response = client.post("/check-age", json={"age": 15})
    assert response.status_code == 200
    assert response.json() == {"status": "not_allowed"}

def test_check_age_negative_value():
    response = client.post('check-age', json={'age': -5})    

    assert response.status_code == 400
    assert response.json()['detail'] == 'age must be non-negative'

def test_check_age_invalid_type():
    response = client.post('/check-age', json={'age': 'abc'})

    assert response.status_code == 422
