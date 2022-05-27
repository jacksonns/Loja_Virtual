from src.models.item import Item
from datetime import timedelta, datetime
from src.util.price_calculator import PriceCalculator

class ShoppingCart(): # Representa um carrinho de compras de uma sessão de usuário
    items: dict[str, dict[str, Item], dict[str, int] ]
    expiration_date: datetime

    def __init__(self, timeout: timedelta = timedelta(days=2)):
        self.expiration_date = datetime.today() + timeout
        self.items = {}

    def is_empty(self) -> bool:
        return not self.items

    def add_item(self, item: Item, quantity: int):
        if item.stock == 0: 
            return
        if item.stock < quantity: 
            quantity = item.stock
        if item.id in self.items:
            self.items[item.id]['quantity'] += quantity
        else:
            self.items[item.id] = {
                'item': item, 
                'quantity': quantity
            }

    def delete_item(self, item: Item):
        del self.items[item.id]
    
    def get_item_quantity(self, item: Item) -> int:
        return self.items[item.id]['quantity']
    
    def get_item_by_id(self, item_id: str) -> Item:
        return self.items[item_id]['item']

    def get_total_price(self) -> tuple[int, int]:
        total_price = (0,0)
        for item_id in self.items:
            item = self.get_item_by_id(item_id)
            result = PriceCalculator.multiply(item.price, self.items[item_id]['quantity'])
            total_price = PriceCalculator.sum(total_price, result)
        return total_price