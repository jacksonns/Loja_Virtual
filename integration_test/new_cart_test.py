from src.app import app
from src.repositories.cart_repo import CartRepository
import pytest
from src.app import db
from src.util.database_utils import delete_last_inserted
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture()
def client_with_cart_teardown(client):
    yield client
    delete_last_inserted("cart")


class TestNewCart:

    def test_new_cart(self, client_with_cart_teardown):
        response = client_with_cart_teardown.post('/cart', follow_redirects=True)
        parsed_response = json.loads(response.get_data(as_text=True))
        cart = CartRepository().get_cart(parsed_response["cart_id"])

        assert cart.id
        assert response.status_code == 200
