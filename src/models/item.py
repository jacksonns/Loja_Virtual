from xmlrpc.client import Boolean
from src.models.user import User
from src.util.price_calculator import PriceCalculator
from src.exceptions.item_exception import InvalidPriceException
from src.exceptions.item_exception import InvalidStockException
from src.exceptions.item_exception import InvalidSaleException

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
        if (self.validatePrice(price)):
            self.price = price
        if (self.validateStock(stock)):
            self.stock = stock
        if (self.validateSale(sale)): 
            self.price = PriceCalculator.apply_sale(self.price, sale)
        else: 
            self.price = price

    def get_price(self) -> tuple[int, int]:
        return self.price
    
    def get_id(self) -> str:
        return self.id
    
    def get_seller(self) -> User:
        return self.seller
    
    def validatePrice(self, price) -> Boolean:
        reais = price[0]
        cents = price[1]
        if((reais < 0) | (cents < 0)):
            raise InvalidPriceException()
        return True

    def validateStock(self, stock) -> Boolean:
        if(stock < 0):
            raise InvalidStockException()
        return True

    def validateSale(self, sale) -> Boolean:
        if(sale < 0):
            raise InvalidSaleException()
        return True