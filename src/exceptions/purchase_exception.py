class NoItemsToBuyException(Exception):
    def __init__(self):
        message = "The shopping cart must contain items to make a purchase."
        super().__init__(message)