class PriceCalculate:

    def sum(price1, price2) -> tuple[int, int]:
        reais = price1[0] + price2[0]
        cents = price1[1] + price2[1]
        while cents >= 100:
            cents -= 100
            reais += 1
        return (reais,cents)

    def multiply(price, quantity) -> tuple[int, int]:
        reais = price[0] * quantity
        cents = price[1] * quantity
        while cents >= 100:
            cents -= 100
            reais += 1
        return (reais, cents)