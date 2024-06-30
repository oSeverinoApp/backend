import pytest

from flask import Flask
from api.todas_as_rotas import rotas_controller
from infraestructure.db_setup import db

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(rotas_controller, url_prefix='/api')
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://severinoapp_test:severinoapp_test@localhost:5434/severinoapp_test_db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_get_user_by_email(client):
    # Test 1
    rv = client.get('/api/get_user_by_email/test@test.com')
    assert b'User not found' in rv.data

def test_create_user(client):
    # Test 2
    rv = client.post('/api/create_user', json={'name': 'Test User', 'email': 'test@test.com', 'state': 'Test State', 'city': 'Test City', 'user_type': '1'})
    assert b'User created successfully!' in rv.data

def test_create_user_existing_email(client):
    # Test 3
    rv = client.post('/api/create_user', json={'name': 'Test User', 'email': 'test@test.com', 'state': 'Test State', 'city': 'Test City', 'user_type': '1'})
    assert b'User already registered.' in rv.data

def test_get_users_by_city(client):
    # Test 4
    rv = client.get('/api/get_users_by_city/Test City')
    assert b'[]' in rv.data

def test_get_users_by_state(client):
    # Test 5
    rv = client.get('/api/get_users_by_state/Test State')
    assert b'[]' in rv.data