from src.models.user import User
from src.exceptions.password_exception import InvalidPasswordException
from src.exceptions.budget_exception import NegativeBudgetException

import pytest

class TestItem:
    
    def test_init_user_with_valid_password(self):
        User('fulano', '123Fulano@')
        
    def test_init_user_with_password_without_upper_case_character(self):
        with pytest.raises(InvalidPasswordException):
            User('fulano', '123fulano@')
    
    def test_init_user_with_password_without_eight_characters(self):
        with pytest.raises(InvalidPasswordException):
            User('fulano', '123Ful@')

    def test_init_user_with_password_without_numeric_characters(self):
        with pytest.raises(InvalidPasswordException):
            User('fulano', 'Fulano!')

    def test_init_user_with_password_without_alphanumeric_characters(self):
        with pytest.raises(InvalidPasswordException):
            User('fulano', '123Fulano')

    def test_get_budget(self):
        user = User('fulano', '123Fulano@')
        assert user.get_budget() == (0,00)

    def test_add_budget(self):
        user = User('fulano', '123Fulano@')
        user.add_budget((1000,00))
        assert user.get_budget() == (1000,00)
    
    def test_subtract_budget(self):
        user = User('fulano', '123Fulano@')
        user.add_budget((1000,00))
        user.subtract_budget((300,00))
        assert user.get_budget() == (700,00)
    
    def test_subtract_budget_throws_negative_budget_exception(self):
        user = User('fulano', '123Fulano@')
        with pytest.raises(NegativeBudgetException):
            user.subtract_budget((300,00))
    
    def test_add_budget_throws_negative_budget_exception(self):
        user = User('fulano', '123Fulano@')
        with pytest.raises(NegativeBudgetException):
            user.add_budget((300,00))
            user.add_budget((-400,00))