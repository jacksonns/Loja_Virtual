from src.util.price_calculator import PriceCalculator

class TestCalculator:

    def test_sum(self):
        assert PriceCalculator.sum((1,00), (1,00)) == (2,00)
        assert PriceCalculator.sum((0,99), (0,99)) == (1,98)
    
    def test_subtraction(self):
        assert PriceCalculator.subtract((3,0), (1,0)) == (2,00)
        assert PriceCalculator.subtract((1,98), (0,99)) == (0,99)

    def test_multiplication(self):
        assert PriceCalculator.multiply((1,00), 2) == (2,00)
        assert PriceCalculator.multiply((0,99), 4) == (3,96)
