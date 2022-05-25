from collections.abc import Callable
from src.models.shopping_cart import ShoppingCart

class Coupon(): # Representa um cupom de desconto.

    code: str

    # Uma função que recebe um carrinho de compras e retorna uma tupla (preço da compra após desconto aplicado)
    # Importante ser do tipo Callable (função) para poder servir descontos progressivos, condicionais, etc. além de descontos simples
    discount: Callable[[ShoppingCart], tuple(int,int)]

    active: bool

    def __init__(self, code: str, discount: Callable[[ShoppingCart], tuple(int,int)], active: bool = True):
        self.code = code
        self.discount = discount
        self.active = active
