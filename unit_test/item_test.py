from src.models.item import Item
from src.models.user import User
from src.exceptions.item_exception import InvalidPriceException
from src.exceptions.item_exception import InvalidStockException
from src.exceptions.item_exception import InvalidSaleException

import pytest

@pytest.fixture
def user():
    user = User('fulano', '123Fulano@')
    yield user

class TestItem:
    def test_init_item_with_negative_price(self, user):
        with pytest.raises(InvalidPriceException):
            Item('I0001', user, 'item1', 'item', (-3,00))

    def test_init_item_with_negative_stock(self, user):
        with pytest.raises(InvalidStockException):
            Item('I0001', user, 'item1', 'item', (3,00), stock=-10)

    def test_init_item_with_negative_sale(self, user):
        with pytest.raises(InvalidSaleException):
            Item('I0001', user, 'item1', 'item', (3,00), stock=0, sale=-10)

    def test_get_price(self, user):
        item = Item('I0001', user, 'item1', 'item', (3,00))
        assert item.get_price() == (3, 00)

    def test_get_id(self, user):
        item = Item('I0001', user, 'item1', 'item', (3,00))
        assert item.get_id() == 'I0001'

    def test_get_seller(self, user):
        item = Item('I0001', user, 'item1', 'item', (3,00))
        assert item.get_seller() == user

    def test_init_item_without_sale(self, user):
        item = Item('I0001', user, 'item1', 'item', (2,50))
        assert item.get_price() == (2, 50)

    def test_init_item_with_exact_sale(self, user):
        item = Item('I0001', user, 'item1', 'item', (2,50), sale=10)
        assert item.get_price() == (2, 25)

    def test_init_item_with_non_exact_sale(self, user):
        item = Item('I0001', user, 'item1', 'item', (2,50), sale=5)
        assert item.get_price() == (2, 37)