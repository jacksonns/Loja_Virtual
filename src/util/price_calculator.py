class PriceCalculator:

    def sum(price1: tuple[int, int], price2: tuple[int,int]) -> tuple[int, int]:
        reais = price1[0] + price2[0] + (price1[1] + price2[1]) // 100
        cents = (price1[1] + price2[1]) % 100
        return (reais,cents)

    def subtract(price1: tuple[int, int], price2: tuple[int,int]) -> tuple[int, int]:
        reais = price1[0] - price2[0] - (1 if price1[1] < price2[1] else 0)
        cents = (price1[1] - price2[1]) + (100 if price1[1] < price2[1] else 0)
        return (reais,cents)

    def multiply(price: tuple[int,int], times: int) -> tuple[int, int]:
        reais = price[0] * times + (price[1] * times) // 100
        cents = (price[1] * times) % 100
        return (reais, cents)