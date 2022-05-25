from src.models.item import Item
from datetime import timedelta, datetime

class ShoppingCart(): # Representa um carrinho de compras de uma sessão de usuário
    items: dict[str, Item, int]
    expiration_date: datetime

    def __init__(self, timeout: timedelta = timedelta(days=2)):
        self.expiration_date = datetime.today() + timeout
        self.items = {}

    def add_item(self, item: Item, quantity: int):
        self.items[item.id] = [Item, quantity]

    def get_total_price(self) -> tuple[int,int]:
        pass