from user import User

class Item(): # Representa um item à venda no marketplace

    seller: User
    name: str
    description: str
    price: tuple(int, int)
    stock: int
    sale: int # Desconto anunciado ao item pelo vendedor, em %

    # TODO: Podemos adicionar informações como tipo de peça, cor...

    def __init__(self, seller: User, name: str, description: str, price: tuple(int, int), stock: int = 1):
        self.seller = seller
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock