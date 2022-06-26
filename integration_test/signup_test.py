from src.app import app
import pytest

from src.repositories.user_repo import UserRepository

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        client.application.app_context().push()
        yield client

class TestSignUp:

    def test_signup_creates_user(self, client):
        username = 'user_test_creates'
        response = client.post('/signup', data={
            'username': username,
            'password': '123Fulano@'
        }, follow_redirects=True)
        user = UserRepository().get_user_by_username(username)
        assert response.status_code == 200
        assert user
        assert user.username == username
        UserRepository().delete_user_by_username(username)

    def test_signup_does_not_accept_existing_username(self, client):
        username = 'user_test_existing'
        response = client.post('/signup', data={
            'username': username,
            'password': '123Fulano@'
        }, follow_redirects=True)
        response = client.post('/signup', data={
            'username': username,
            'password': '123Ciclano@'
        }, follow_redirects=True)

        assert response.status_code == 409

        UserRepository().delete_user_by_username(username)
        user = UserRepository().get_user_by_username(username)
        assert not user

class TestSignUp2:
    def test_signup_does_not_accept_lower_case_password(self, client):
        username = 'user_test_lowercase'
        response = client.post('/signup', data={
            'username': username,
            'password': '123fulano@'
        }, follow_redirects=False)
        assert response.status_code == 422
        user = UserRepository().get_user_by_username(username)
        assert not user
    
    def test_signup_does_not_accept_small_password(self, client):
        username = 'user_test_small_password'
        response = client.post('/signup', data={
            'username': username,
            'password': '123Ful@'
        }, follow_redirects=False)
        assert response.status_code == 422
        user = UserRepository().get_user_by_username(username)
        assert not user

    def test_signup_does_not_accept_password_without_numeric_characters(self, client):
        username = 'user_test_without_numeric'
        response = client.post('/signup', data={
            'username': username,
            'password': 'Fulano!'
        }, follow_redirects=False)
        assert response.status_code == 422
        user = UserRepository().get_user_by_username(username)
        assert not user

    def test_signup_does_not_accept_password_without_special_characters(self, client):
        username = 'user_test_without_special'
        response = client.post('/signup', data={
            'username': username,
            'password': '123Fulano'
        }, follow_redirects=False)
        assert response.status_code == 422
        user = UserRepository().get_user_by_username(username)
        assert not user