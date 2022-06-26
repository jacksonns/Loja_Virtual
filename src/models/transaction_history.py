from datetime import datetime
import uuid


class TransactionHistory: #Guarda o histórico de compras/vendas
    seller_id: uuid.UUID
    buyer_id: uuid.UUID
    cart_id: uuid.UUID
    shipping_cost: tuple[int, int]
    items_cost: tuple[int, int]
    total_cost: tuple[int, int]
    purchase_date: str

    def __init__(self, buyer_id: uuid.UUID):
        self.buyer_id = buyer_id

    def set_purchase_date(self):
        self.purchase_date = datetime.now().strftime("%d/%m/%y %H:%M")

    def set_transaction_details(self, seller_id, cart_id, shipping_cost, items_cost, total_cost):
        self.seller_id = seller_id
        self.cart_id = cart_id
        self.shipping_cost = shipping_cost
        self.items_cost = items_cost
        self.total_cost = total_cost



