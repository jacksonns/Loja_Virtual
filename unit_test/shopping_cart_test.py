from src.models.item import Item
from src.models.shopping_cart import ShoppingCart
from src.models.user import User

import pytest

@pytest.fixture
def user():
    user = User('fulano', '123')
    yield user

@pytest.fixture
def cart():
    cart = ShoppingCart()
    yield cart


class TestShoppingCart:
    
    def test_add_item(self, user, cart):
        item = Item('I0001', user, 'item1', 'item', (1,99))
        cart.add_item(item, 1)
        assert item.id in cart.items