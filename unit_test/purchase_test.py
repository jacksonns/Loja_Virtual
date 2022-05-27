from src.models.item import Item
from src.models.shopping_cart import ShoppingCart
from src.models.user import User
from src.models.session import Session
from src.models.purchase import Purchase
from src.models.address import Address

import pytest

@pytest.fixture
def session():
    user = User('fulano', '123')
    session = Session(user)
    yield session

@pytest.fixture
def br_address():
    address = Address(country="Brasil", state="MG", city="Belo Horizonte", postal_code="99999-333", street_address="Av. XXXXXX 351")
    yield address

@pytest.fixture
def intl_address():
    address = Address(country="United States", state="New York", city="New York City", postal_code="10001", street_address="13th St. 47 W")
    yield address

@pytest.fixture
def item_costing_100():
    item = Item('I0001', User('fulano', '123'), 'item1', 'item', (100,00), stock=10)
    yield item

class TestPurchase:

    def test_free_shipping_for_br(self, session: Session, br_address: Address, item_costing_100: Item):
        session.cart.add_item(item_costing_100, 2)
        assert Purchase(session, br_address).get_shipping_rate() == (0,0)
    
    def test_no_free_shipping_for_intl(self, session: Session, intl_address: Address, item_costing_100: Item):
        session.cart.add_item(item_costing_100,2)
        assert Purchase(session, intl_address).get_shipping_rate() > (0,0)

    def test_shipping_rate_for_br(self, session: Session, br_address: Address, item_costing_100: Item):
        session.cart.add_item(item_costing_100, 1)
        assert Purchase(session, br_address).get_shipping_rate() == (5,0)

    def test_shipping_rate_for_intl(self, session: Session, intl_address: Address, item_costing_100: Item):
        session.cart.add_item(item_costing_100, 1)
        assert Purchase(session, intl_address).get_shipping_rate() == (15,0)