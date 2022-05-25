class PriceCalculate:

    def sum(price1, price2) -> tuple[int, int]:
        result = tuple()
        result[0] = price1[0] + price2[0]
        result[1] = price1[1] + price2[1]
        while result[1] >= 100:
            result[1] -= 100
            result[0] += 1
        return result

    def multiply(price, quantity) -> tuple[int, int]:
        result = tuple()
        result[0] = price[0] * quantity
        result[1] = price[1] * quantity
        while result[1] >= 100:
            result[1] -= 100
            result[0] += 1
        return result