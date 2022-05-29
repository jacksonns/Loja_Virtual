from src.models.shipping_rate_policy import ShippingRatePolicy
from src.models.address import Address


class ShippingRateCalculator:
    shipping_rate_add_op: [ShippingRatePolicy]
    shipping_rate_mult_op: [ShippingRatePolicy]

    def include_shipping_rate_policy(self, shipping_rate: ShippingRatePolicy):
        if shipping_rate.shipping_rate_op == ShippingRatePolicy.SHIPPING_RATE_OP_ADD:
            self.shipping_rate_add_op.append(shipping_rate)
        else:
            self.shipping_rate_mult_op.append(shipping_rate)

    def get_shipping_rate(self, sender_address: Address, receiver_address: Address):
        current_shipping_rate = (0, 0)

        for add_shipping_rate in self.shipping_rate_add_op:
            current_shipping_rate = add_shipping_rate.apply_shipping_rate(current_shipping_rate, sender_address,
                                                                          receiver_address)

        for mult_shipping_rate in self.shipping_rate_mult_op:
            current_shipping_rate = mult_shipping_rate.apply_shipping_rate(current_shipping_rate, sender_address,
                                                                           receiver_address)

        return current_shipping_rate
