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