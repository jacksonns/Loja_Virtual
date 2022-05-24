from datetime import datetime, timedelta
from user import User
from shopping_cart import ShoppingCart
from datetime import datetime, timedelta

class Session(): # Representa uma sessão de usuário logado.
    
    user: User
    expiration_date: timedelta
    cart: ShoppingCart

    def __init__(self, user: User, timeout: timedelta = timedelta(days=7) ):
        self.user = user
        self.expiration_date = datetime.today() + timeout
        self.cart = ShoppingCart()

