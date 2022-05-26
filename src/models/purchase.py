from src.models.session import Session
from src.models.coupon import Coupon
from src.models.address import Address

class Purchase(): # Representa uma operação de compra feita na loja

    session: Session
    applied_coupon: Coupon
    delivery_address: Address

    def __init__(self, session: Session, delivery_address: Address, applied_coupon: Coupon = None):
        self.session = session
        self.delivery_address = delivery_address
        self.applied_coupon = applied_coupon

    # Por enquanto, o cálculo do frete é algo simples e não corresponde à realidade
    def get_shipping_rate(self) -> tuple[int,int]:
        if (self.delivery_address.country != 'Brasil'): # Compras internacionais
            return (15,0)
        elif (self.session.cart.get_total_price() >= (200,0)): # Frete grátis para compras acima de $200
            return (0,0)
        else:
            return (5,0)

    def get_total_price(self):
        price = self.session.cart.get_total_price()
        return price