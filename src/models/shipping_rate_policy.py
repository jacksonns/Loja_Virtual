import abc
from src.models.address import Address
from src.util.price_calculator import PriceCalculator


class ShippingRatePolicy(metaclass=abc.ABCMeta):
    shipping_rate_op: int
    SHIPPING_RATE_OP_ADD = 1
    SHIPPING_RATE_OP_MULT = 2

    @abc.abstractmethod
    def apply_shipping_rate(self, current_rate_value: tuple, sender_address: Address, receiver_address: Address):
        return


class FreeShippingForCountryPolicy(ShippingRatePolicy):
    country: str

    def __init__(self, country):
        self.country = country
        self.shipping_rate_op = ShippingRatePolicy.SHIPPING_RATE_OP_MULT

    def apply_shipping_rate(self, current_rate_value: tuple, sender_address: Address, receiver_address: Address):
        return (0, 0) if receiver_address.country == self.country else current_rate_value


class SeasonalDiscountPolicy(ShippingRatePolicy):
    discount: tuple

    def __init__(self, discount):
        self.discount = discount
        self.shipping_rate_op = ShippingRatePolicy.SHIPPING_RATE_OP_ADD

    def apply_shipping_rate(self, current_rate_value: tuple, sender_address: Address, receiver_address: Address):
        return PriceCalculator.subtract(current_rate_value, self.discount)

class DefaultShippingRate(ShippingRatePolicy):
    value: tuple

    def __init__(self, value):
        self.value = value
        self.shipping_rate_op = ShippingRatePolicy.SHIPPING_RATE_OP_ADD

    def apply_shipping_rate(self, current_rate_value: tuple, sender_address: Address, receiver_address: Address):
        return PriceCalculator.sum(current_rate_value, self.value)
