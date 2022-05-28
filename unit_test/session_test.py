from src.models.user import User
from src.models.session import Session
from src.models.item import Item
from src.exceptions.budget_exception import NegativeBudgetException

import pytest

@pytest.fixture
def session():
    user = User('fulano', '123Fulano@')
    session = Session(user)
    yield session

@pytest.fixture
def seller1():
    seller1 = User('beltrano', '456Beltrano@')
    yield seller1

class TestPurchase:

    def test_get_user_budget(self, session: Session):
        assert session.get_user_budget() == (0,00)

    def test_add_user_budget(self, session: Session):
        session.add_user_budget((1000,00))
        assert session.get_user_budget() == (1000,00)
    
    def test_subtract_user_budget(self, session: Session):
        session.add_user_budget((1000,00))
        session.subtract_user_budget((300,00))
        assert session.get_user_budget() == (700,00)
    
    def test_subtract_user_budget_throws_negative_budget_exception(self, session: Session):
        with pytest.raises(NegativeBudgetException):
            session.subtract_user_budget((300,00))
    
    def test_add_user_budget_throws_negative_budget_exception(self, session: Session):
        with pytest.raises(NegativeBudgetException):
            session.add_user_budget((300,00))
            session.add_user_budget((-400,00))

    def test_get_cart_items_with_zero_itens_in_cart(self, session: Session):
        assert len(session.get_cart_items()) == 0
    
    def test_get_cart_items_with_one_item_in_cart(self, session: Session):
        item = Item('I0001', seller1, 'item1', 'item', (100,00))
        session.cart.add_item(item, 1)
        assert len(session.get_cart_items()) == 1
