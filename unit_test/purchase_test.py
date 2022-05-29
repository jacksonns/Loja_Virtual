from src.models.item import Item
from src.models.user import User
from src.models.session import Session
from src.models.purchase import Purchase
from src.models.address import Address
from src.util.price_calculator import PriceCalculator
from src.exceptions.budget_exception import InsufficientBudgetException
from src.exceptions.purchase_exception import NoItemsToBuyException

import pytest

@pytest.fixture
def session():
    user = User('fulano', '123Fulano@')
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
    item = Item('I0001', User('fulano', '123Fulano@'), 'item1', 'item', (100,00), stock=10)
    yield item

@pytest.fixture
def seller1():
    seller1 = User('beltrano', '456Beltrano@')
    yield seller1

@pytest.fixture
def seller2():
    seller2 = User('sicrano', '789Sicrano@')
    yield seller2

@pytest.fixture
def purchase_br(session, br_address):
    purchase = Purchase(session, br_address)
    yield purchase


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
    
    def test_make_purchase_with_insufficient_budget(self, session, seller1, br_address):
        item = Item('I0001', seller1, 'item1', 'item', (100,00))
        session.cart.add_item(item, 1)
        purchase = Purchase(session, br_address)
        with pytest.raises(InsufficientBudgetException):
            purchase.make_purchase()
    
    def test_user_budget_after_purchase(self, purchase_br, seller1):
        purchase_br.session.add_user_budget((1000,00))
        item = Item('I0001', seller1, 'item1', 'item', (100,00), stock=10)
        purchase_br.session.cart.add_item(item, 3)
        purchase_br.make_purchase()
        assert purchase_br.session.get_user_budget() == (700,00)
    
    def test_seller_budget_after_purchase_with_one_seller(self, purchase_br, seller1):
        purchase_br.session.add_user_budget((1000,00))
        item = Item('I0001', seller1, 'item1', 'item', (100,00), stock=10)
        purchase_br.session.cart.add_item(item, 3)
        purchase_br.make_purchase()
        assert seller1.get_budget() == (300,00)

    def test_seller_budget_after_purchase_with_more_sellers(self, purchase_br, seller1, seller2):
        purchase_br.session.add_user_budget((1000,00))
        item1 = Item('I0001', seller1, 'item1', 'item', (100,00), stock=10)
        item2 = Item('I0002', seller2, 'item2', 'item', (200,00), stock=10)
        purchase_br.session.cart.add_item(item1, 2)
        purchase_br.session.cart.add_item(item2, 1)
        purchase_br.make_purchase()
        assert seller1.get_budget() == (200,00)
        assert seller2.get_budget() == (200,00)

    def test_purchase_with_empty_shopping_cart(self, purchase_br):
        purchase_br.session.add_user_budget((1000,00))
        with pytest.raises(NoItemsToBuyException):
            purchase_br.make_purchase()

    def test_transaction_history_after_purchase_with_one_seller(self, purchase_br, seller1):
        purchase_br.session.add_user_budget((1000,00))
        item = Item('I0001', seller1, 'item1', 'item', (100,00), stock=10)
        item2 = Item('I0002', seller1, 'item2', 'item', (250,00), stock=10)

        purchase_br.session.cart.add_item(item, 3)
        purchase_br.session.cart.add_item(item2, 2)

        transaction_history = purchase_br.make_purchase()

        assert transaction_history[0].buyer_id == purchase_br.session.user.id
        assert transaction_history[0].seller_id == seller1.id
        assert transaction_history[0].cart_id == purchase_br.session.cart.id
        assert transaction_history[0].shipping_cost == purchase_br.get_shipping_rate()
        assert transaction_history[0].items_cost == (800,00)
        assert transaction_history[0].total_cost == PriceCalculator.sum((800, 00), purchase_br.get_shipping_rate())

    def test_transaction_history_after_purchase_with_multiple_sellers(self, purchase_br, seller1, seller2):
        purchase_br.session.add_user_budget((1000,00))
        item = Item('I0001', seller1, 'item1', 'item', (100,00), stock=10)
        item2 = Item('I0002', seller2, 'item2', 'item', (250,00), stock=10)

        purchase_br.session.cart.add_item(item, 3)
        purchase_br.session.cart.add_item(item2, 2)

        transaction_history = purchase_br.make_purchase()

        assert transaction_history[0].buyer_id == purchase_br.session.user.id
        assert transaction_history[0].seller_id == seller1.id
        assert transaction_history[0].cart_id == purchase_br.session.cart.id
        assert transaction_history[1].buyer_id == purchase_br.session.user.id
        assert transaction_history[1].seller_id == seller2.id
        assert transaction_history[1].cart_id == purchase_br.session.cart.id

        assert transaction_history[0].shipping_cost == purchase_br.get_shipping_rate()
        assert transaction_history[0].items_cost == (300,00)
        assert transaction_history[0].total_cost == PriceCalculator.sum((300, 00), purchase_br.get_shipping_rate())
        assert transaction_history[1].shipping_cost == purchase_br.get_shipping_rate()
        assert transaction_history[1].items_cost == (500,00)
        assert transaction_history[1].total_cost == PriceCalculator.sum((500, 00), purchase_br.get_shipping_rate())
