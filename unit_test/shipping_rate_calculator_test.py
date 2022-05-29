from src.models.address import Address
from src.models.shipping_rate_policy import *
from src.util.shipping_rate_calculator import ShippingRateCalculator

import pytest


@pytest.fixture
def shipping_rate_calculator():
    yield ShippingRateCalculator()


@pytest.fixture
def br_address():
    address = Address(country="Brasil", state="MG", city="Belo Horizonte", postal_code="99999-333",
                      street_address="Av. XXXXXX 351")
    yield address


@pytest.fixture
def intl_address():
    address = Address(country="United States", state="New York", city="New York City", postal_code="10001",
                      street_address="13th St. 47 W")
    yield address


class TestShippingRateCalculator:

    def test_default_shipping_rate(self, shipping_rate_calculator, intl_address):
        default_shipping_policy = DefaultShippingRate((15, 0))

        shipping_rate_calculator.include_shipping_rate_policy(default_shipping_policy)

        rate = shipping_rate_calculator.get_shipping_rate(br_address, intl_address)

        assert rate == (15, 0)

    def test_get_shipping_rate_for_country_with_free_shipping(self, shipping_rate_calculator, br_address):
        free_shipping_policy = FreeShippingForCountryPolicy("Brasil")
        default_shipping_policy = DefaultShippingRate((15, 0))

        shipping_rate_calculator.include_shipping_rate_policy(free_shipping_policy)
        shipping_rate_calculator.include_shipping_rate_policy(default_shipping_policy)

        rate = shipping_rate_calculator.get_shipping_rate(br_address, br_address)

        assert rate == (0, 0)

    def test_get_shipping_rate_for_country_without_free_shipping(self, shipping_rate_calculator, br_address):
        free_shipping_policy = FreeShippingForCountryPolicy("Argentina")
        default_shipping_policy = DefaultShippingRate((15, 0))

        shipping_rate_calculator.include_shipping_rate_policy(free_shipping_policy)
        shipping_rate_calculator.include_shipping_rate_policy(default_shipping_policy)

        rate = shipping_rate_calculator.get_shipping_rate(br_address, br_address)

        assert rate == (15, 0)


    def test_get_shipping_rate_discount(self, shipping_rate_calculator, br_address):
        discount_shipping_rate = SeasonalDiscountPolicy((20,0))
        default_shipping_policy = DefaultShippingRate((30, 0))

        shipping_rate_calculator.include_shipping_rate_policy(discount_shipping_rate)
        shipping_rate_calculator.include_shipping_rate_policy(default_shipping_policy)

        rate = shipping_rate_calculator.get_shipping_rate(br_address, br_address)

        assert rate == (10, 0)

    def test_get_shipping_rate_discount_when_its_surpasses_the_current_rate(self, shipping_rate_calculator, br_address):
        discount_shipping_rate = SeasonalDiscountPolicy((20, 0))
        default_shipping_policy = DefaultShippingRate((10, 0))

        shipping_rate_calculator.include_shipping_rate_policy(discount_shipping_rate)
        shipping_rate_calculator.include_shipping_rate_policy(default_shipping_policy)

        rate = shipping_rate_calculator.get_shipping_rate(br_address, br_address)

        assert rate == (0, 0)
