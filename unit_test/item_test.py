from src.models.item import Item
from src.models.user import User

import pytest

@pytest.fixture
def user():
    user = User('fulano', '123')
    yield user

class TestItem:

    def test_init_item_without_sale(self, user):
        item = Item('I0001', user, 'item1', 'item', (2,50))
        assert item.price == (2, 50)

    def test_init_item_with_exact_sale(self, user):
        item = Item('I0001', user, 'item1', 'item', (2,50), sale=10)
        assert item.price == (2, 25)

    def test_init_item_with_non_exact_sale(self, user):
        item = Item('I0001', user, 'item1', 'item', (2,50), sale=5)
        assert item.price == (2, 37)