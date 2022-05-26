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

    def test_add_item_that_already_exists(self, user, cart):
        item = Item('I0001', user, 'item1', 'item', (1,99))
        cart.add_item(item, 1)
        cart.add_item(item, 1)
        assert cart.get_item_quantity(item) == 2

    def test_cart_is_empty_after_delete(self, user, cart):
        item = Item('I0001', user, 'item1', 'item', (1,99))
        cart.add_item(item, 1)
        cart.delete_item(item)
        assert cart.is_empty()

    def test_get_total_cart_price(sef, user, cart):
        item1 = Item('I0001', user, 'item1', 'item', (1,99))
        item2 = Item('I0002', user, 'item2', 'item', (2,00))
        cart.add_item(item1, 2)
        cart.add_item(item2, 1)
        assert cart.get_total_price() == (5,98)