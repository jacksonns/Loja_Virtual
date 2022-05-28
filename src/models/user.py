from src.util.price_calculator import PriceCalculator
from src.exceptions.budget_exception import NegativeBudgetException
from src.exceptions.password_exception import InvalidPasswordException
import time

class User():
    id: int
    username: str
    password: str
    budget: tuple[int, int]

    def __init__(self, username: str, password: str, budget: tuple[int, int] = (0,0)):
        self.id = int(time.time())
        self.username = username
        self.budget = budget
        if (self.validatePassword(password)):
            self.password = password
    
    def get_budget(self) -> tuple[int, int]:
        return self.budget
    
    def add_budget(self, quantity: tuple[int, int]):
        result = PriceCalculator.sum(self.budget, quantity)
        if (result < (0,0)):
            raise NegativeBudgetException()
        else:
            self.budget = result
    
    def subtract_budget(self, quantity: tuple[int, int]):
        result = PriceCalculator.subtract(self.budget, quantity)
        if (result < (0,0)):
            raise NegativeBudgetException()
        else:
            self.budget = result

    def validatePassword(self, password):
        if(password.islower() | (len(password) <= 7) | password.isalpha() | password.isalnum()):
            raise InvalidPasswordException(password)
        return True
