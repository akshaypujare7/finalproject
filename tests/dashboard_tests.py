from flask import url_for


def test_register(client):
    """This tests for successful registration"""
    with client:
        response = client.post("/register", data={
            "email": "akshay@gmail",
            "password": "akshay123",
            "confirm": "akshay123"
        }, follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == url_for('auth.login')


def test_login(client):
    """This tests for successful login"""
    with client:
        response = client.post("/register", data={
            "email": "akshay@gmail",
            "password": "akshay123",
            "confirm": "akshay123"
        }, follow_redirects=True)

        assert response.status_code == 200
        assert response.request.path == url_for('auth.login')

        login_response = client.post("/login", data={
            "email": "akshay@gmail",
            "password": "akshay123",
        }, follow_redirects=True)
        assert login_response.request.path == url_for('auth.dashboard')
        assert login_response.status_code == 200


def test_dashboard_access_success(client):
    """This tests for successful access to dashboard after login"""
    with client:
        login_response = client.post("/login", data={
            "email": "akshay@gmail",
            "password": "akshay123",
        }, follow_redirects=True)
        assert login_response.request.path == url_for('auth.dashboard')
        assert login_response.status_code == 200


def test_dashboard_access_denied(client):
    """This tests for unsuccessful access to dashboard after login"""
    with client:
        response = client.post("/register", data={
            "email": "akshay@gmail",
            "password": "akshay123",
            "confirm": "akshay123"
        }, follow_redirects=True)

        assert response.status_code == 200
        assert response.request.path == url_for('auth.login')

        login_response = client.post("/login", data={
            "email": "akshay@gmail",
            "password": "akshay123",
        }, follow_redirects=True)
        assert login_response.request.path == url_for('auth.login')
        assert login_response.status_code == 200
