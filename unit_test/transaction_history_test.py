import pytest
from src.models.transaction_history import TransactionHistory
from src.models.user import User
from src.models.shopping_cart import ShoppingCart
from src.models.item import Item

@pytest.fixture
def buyer():
    user = User('fulano', '123Fulano@')
    yield user

@pytest.fixture
def seller():
    user = User('ciclano', '123Fulano@')
    yield user

@pytest.fixture
def cart(seller):
    cart = ShoppingCart()
    cart.add_item(Item('I0001', seller, 'item1', 'item', (1, 99)), 1)

    yield cart

class TestTransactionHistory:
    def test_init_transaction_history(self, buyer):
        transaction_history = TransactionHistory(buyer.id)
        assert buyer.id == transaction_history.buyer_id

    def test_set_transaction_details(self, buyer, seller, cart):
        transaction_history = TransactionHistory(buyer.id)
        transaction_history.set_transaction_details(seller.id, cart.id, (10, 0), (99, 20), (109, 20))

        assert transaction_history.seller_id == seller.id
        assert transaction_history.cart_id == cart.id
        assert transaction_history.shipping_cost == (10, 0)
        assert transaction_history.items_cost == (99, 20)
        assert transaction_history.total_cost == (109, 20)