from item import Item
from datetime import timedelta, datetime

class ShoppingCart(): # Representa um carrinho de compras de uma sessão de usuário
    items: dict[Item, int]
    expiration_date: datetime

    def __init__(self, timeout: timedelta = timedelta(days=2)):
        self.expiration_date = datetime.today() + timeout
