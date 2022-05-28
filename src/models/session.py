from datetime import datetime, timedelta
from src.models.user import User
from src.models.shopping_cart import ShoppingCart

class Session(): # Representa uma sessão de usuário logado.
    
    user: User
    expiration_date: timedelta
    cart: ShoppingCart

    def __init__(self, user: User, timeout: timedelta = timedelta(days=7) ):
        self.user = user
        self.expiration_date = datetime.today() + timeout
        self.cart = ShoppingCart()
    
    def get_user_budget(self) -> tuple[int, int]:
        return self.user.get_budget()
    
    def get_cart_items(self):
        return self.cart.get_items()
    
    def add_user_budget(self, quantity: tuple[int, int]):
        self.user.add_budget(quantity)
    
    def subtract_user_budget(self, quantity: tuple[int, int]):
        self.user.subtract_budget(quantity)