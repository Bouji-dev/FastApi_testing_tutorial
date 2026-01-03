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