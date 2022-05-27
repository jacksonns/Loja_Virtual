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
    
    def apply_sale(price: tuple[int, int], sale: int) -> tuple[int, int]:
        real_price = float('.'.join(str(num) for num in price))
        new_price = round(real_price * ((100 - sale) / 100), 2)
        reais = int(new_price)
        cents = int((new_price - reais)*100)
        return (reais, cents)
