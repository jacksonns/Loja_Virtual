from datetime import datetime

class TransactionHistory: #Guarda o histórico de compras/vendas
    seller_id: int
    buyer_id: int
    cart_id: int
    shipping_cost: int
    items_cost: int
    total_cost: int
    purchase_date: str

    def __init__(self, buyer_id: int):
        self.buyer_id = buyer_id

    def set_purchase_date(self):
        self.purchase_date = datetime.now().strftime("%d/%m/%y %H:%M")

    def set_transaction_details(self, seller_id, cart_id, shipping_cost, items_cost, total_cost):
        self.seller_id = seller_id
        self.cart_id = cart_id
        self.shipping_cost = shipping_cost
        self.items_cost = items_cost
        self.total_cost = total_cost



