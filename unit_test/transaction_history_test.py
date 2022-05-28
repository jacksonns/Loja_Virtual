import pytest
from src.models.transaction_history import TransactionHistory
from src.models.user import User

@pytest.fixture
def buyer():
    user = User('fulano', '123Fulano@')
    yield user

@pytest.fixture
def seller():
    user = User('ciclano', '123456')
    yield user

class TransactionHistory():
    def init_transaction_history(self, buyer):
        transaction_history = TransactionHistory(buyer.id)
        assert buyer.id == transaction_history.buyer_id

    def set_transaction_details(self, buyer, seller):
        transaction_history = TransactionHistory(buyer.id)
        assert buyer.id == transaction_history.buyer_id