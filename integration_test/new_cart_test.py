from src.app import app
from src.repositories.cart_repo import CartRepository
import pytest
from src.app import db
from src.util.database_utils import delete_last_inserted
import json
from datetime import datetime
from src.database.tables import CartTable

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        client.application.app_context().push()
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

    def test_get_cart(self, client_with_cart_teardown):
        expiration_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        new_cart = CartTable("test-id-0001", expiration_date)
        db.session.add(new_cart)
        db.session.commit()

        response = client_with_cart_teardown.get('/cart?id=test-id-0001', follow_redirects=True)
        parsed_response = json.loads(response.get_data(as_text=True))

        assert parsed_response["cart_id"] == "test-id-0001"
        assert parsed_response["expiration_date"] == expiration_date
        assert response.status_code == 200