from src.util.price_calculator import PriceCalculator

class User():

    username: str
    password: str
    budget: tuple[int, int]

    def __init__(self, username: str, password: str, budget: tuple[int, int] = (0,0)):
        self.username = username
        self.password = password
        self.budget = budget
    
    def get_budget(self) -> tuple[int, int]:
        return self.budget
    
    def add_budget(self, quantity: tuple[int, int]):
        self.budget = PriceCalculator.sum(self.budget, quantity)
    
    def subtract_budget(self, quantity: tuple[int, int]):
        self.budget = PriceCalculator.subtract(self.budget, quantity)