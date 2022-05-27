from src.models.user import User
from src.util.price_calculator import PriceCalculator

class Item(): # Representa um item à venda no marketplace

    id: str
    seller: User
    name: str
    description: str
    price: tuple[int, int]
    stock: int
    sale: int # Desconto anunciado ao item pelo vendedor, em %

    # TODO: Podemos adicionar informações como tipo de peça, cor...

    def __init__(self, id: str, seller: User, name: str, description: str, price: tuple[int, int], stock: int = 1, sale: int = 0):
        self.id = id
        self.seller = seller
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.sale = sale
        if sale: 
            self.price = PriceCalculator.apply_sale(self.price, sale)
        else: 
            self.price = price

    def get_price(self) -> tuple[int, int]:
        return self.price
    
    def get_id(self) -> str:
        return self.id