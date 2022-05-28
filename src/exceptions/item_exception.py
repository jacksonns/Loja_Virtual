class InvalidPriceException(Exception):
    def __init__(self):
        message = "Item value must not be less than 0."
        super().__init__(message)

class InvalidStockException(Exception):
    def __init__(self):
        message = "Item stock must not be less than 0."
        super().__init__(message)

class InvalidSaleException(Exception):
    def __init__(self):
        message = "Item sale must not be less than 0."
        super().__init__(message)