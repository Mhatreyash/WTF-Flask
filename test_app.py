import pytest
from flask import url_for
from wtf import create_app
from wtf.models import db, User
from werkzeug.security import check_password_hash

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.app_context():
        db.create_all()
    
    yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Home Page' in response.data

def test_register_page(client):
    response = client.get('/auth/register')
    assert response.status_code == 200
    assert b'Register' in response.data

def test_login_page(client):
    response = client.get('/auth/login')
    assert response.status_code == 200
    assert b'Login' in response.data

def test_user_registration(client, app):
    response = client.post('/auth/register', data={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword',
        'confirm_password': 'testpassword'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Login' in response.data
    
    with app.app_context():
        user = User.query.filter_by(username='testuser').first()
        assert user is not None
        assert user.email == 'testuser@example.com'
        assert check_password_hash(user.password, 'testpassword')

def test_user_login(client, app):
    # First, register a user
    client.post('/auth/register', data={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword',
        'confirm_password': 'testpassword'
    })
    
    # Then, try to log in
    response = client.post('/auth/login', data={
        'email': 'testuser@example.com',
        'password': 'testpassword'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Profile Page' in response.data
    assert b'testuser' in response.data

def test_profile_page_access(client, app):
    # Register and log in a user
    client.post('/auth/register', data={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword',
        'confirm_password': 'testpassword'
    })
    client.post('/auth/login', data={
        'email': 'testuser@example.com',
        'password': 'testpassword'
    })
    
    # Access the profile page
    response = client.get('/auth/profile')
    assert response.status_code == 200
    assert b'Profile Page' in response.data
    assert b'testuser' in response.data

def test_logout(client, app):
    # Register and log in a user
    client.post('/auth/register', data={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword',
        'confirm_password': 'testpassword'
    })
    client.post('/auth/login', data={
        'email': 'testuser@example.com',
        'password': 'testpassword'
    })
    
    # Logout
    response = client.get('/auth/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data

def test_404_error(client):
    response = client.get('/nonexistent-page')
    assert response.status_code == 404
    assert b'Error : 404' in response.data