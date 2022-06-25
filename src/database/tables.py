from src.app import db

class User(db.Model):
    
    __tablename__ = 'user'

    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    budget_reais = db.Column(db.Integer, nullable=False)
    budget_cents = db.Column(db.Integer, nullable=False)


class Item(db.Model):

    __tablename__ = 'item'

    id = db.Column(db.String, primary_key=True)
    seller_id = db.Column(db.String, db.ForeignKey('user.id'))
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    price_reais = db.Column(db.Integer, nullable=False)
    price_cents = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    sale = db.Column(db.Integer)


class ItemList(db.Model):

    __tablename__ = 'item_list'

    id = db.Column(db.String, primary_key=True)
    item_id = db.Column(db.String, db.ForeignKey('item.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)


class Cart(db.Model):

    __tablename__ = 'cart'

    id = db.Column(db.String, primary_key=True)
    item_list = db.Column(db.String, db.ForeignKey('item_list.id'))
    expiration_date = db.Column(db.String)


class Session(db.Model):

    __tablename__ = 'session'

    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.id'))
    expiration_date = db.Column(db.String)
    cart_id = db.Column(db.String, db.ForeignKey('cart.id'))
