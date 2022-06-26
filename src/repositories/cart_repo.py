from src.database.tables import CartTable, CartItemTable
from src.models.item import Item
from src.repositories.user_repo import UserRepository
from src.app import db
import datetime
from src.models.shopping_cart import ShoppingCart

class CartRepository:
    def create_cart(self, cart):
        new_cart = CartTable(cart.id.hex, cart.expiration_date.strftime("%m/%d/%Y, %H:%M:%S"))
        db.session.add(new_cart)
        db.session.commit()

        return new_cart.id

    def get_cart(self, cart_id):
        cart = db.session.query(CartTable).filter(CartTable.id == cart_id).first()

        if cart:
            found_cart = ShoppingCart()
            found_cart.id = cart.id
            found_cart.expiration_date = cart.expiration_date
            return found_cart

        return None