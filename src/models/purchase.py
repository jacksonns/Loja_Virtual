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