from src.models.session import Session
from src.models.coupon import Coupon
from src.models.address import Address
from src.models.transaction_history import TransactionHistory
from src.util.price_calculator import PriceCalculator
from src.exceptions.budget_exception import InsufficientBudgetException

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

    def make_payment(self, total_price):
        self.session.subtract_user_budget(total_price)

    def update_sellers_budget(self):
        for item_id in self.session.get_cart_items():
            item = self.session.cart.get_item_by_id(item_id)
            seller = item.get_seller()
            payed_value = self.session.cart.get_total_price_of_item(item)
            seller.add_budget(payed_value)

    def log_transaction_history(self):
        sellers_with_costs = dict()
        buyer_id = self.session.user.id
        cart_id = self.session.cart.id

        for item_id in self.session.get_cart_items():
            item = self.session.cart.get_item_by_id(item_id)
            payed_value = self.session.cart.get_total_price_of_item(item)
            seller_id = item.get_seller().id

            if seller_id not in sellers_with_costs:
                sellers_with_costs[seller_id] = dict()
                sellers_with_costs[seller_id]["shipping_cost"] = self.get_shipping_rate()
                sellers_with_costs[seller_id]["items_cost"] = (0, 0)
                sellers_with_costs[seller_id]["total_cost"] = (0, 0)

            sellers_with_costs[seller_id]["items_cost"] = PriceCalculator.sum(sellers_with_costs[seller_id]["items_cost"], payed_value)
            sellers_with_costs[seller_id]["total_cost"] = PriceCalculator.sum(sellers_with_costs[seller_id]["total_cost"], payed_value)

        history = []
        for seller_id, seller_costs in sellers_with_costs.items():
            transaction_history = TransactionHistory(buyer_id)
            transaction_history.set_transaction_details(seller_id, cart_id, seller_costs["shipping_cost"], seller_costs["items_cost"], seller_costs["total_cost"])
            history.append(transaction_history)

        return history

    def make_purchase(self):
        if self.session.get_user_budget() < self.get_total_price():
            raise InsufficientBudgetException
        else:
            self.make_payment(self.get_total_price())
            self.update_sellers_budget()
            return self.log_transaction_history()
