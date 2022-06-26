from src.app import db

class UserTable(db.Model):
    
    __tablename__ = 'user'

    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    budget_reais = db.Column(db.Integer, nullable=False)
    budget_cents = db.Column(db.Integer, nullable=False)


class ItemTable(db.Model):

    __tablename__ = 'item'

    id = db.Column(db.String, primary_key=True)
    seller_id = db.Column(db.String, db.ForeignKey('user.id'))
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    price_reais = db.Column(db.Integer, nullable=False)
    price_cents = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    sale = db.Column(db.Integer)


class CartItemTable(db.Model):

    __tablename__ = 'cart_item'

    id = db.Column(db.String, primary_key=True)
    item_id = db.Column(db.String, db.ForeignKey('item.id'), primary_key=True)
    cart_id = db.Column(db.String, db.ForeignKey('cart.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)


class CartTable(db.Model):

    __tablename__ = 'cart'

    id = db.Column(db.String, primary_key=True)
    expiration_date = db.Column(db.String)


class SessionTable(db.Model):

    __tablename__ = 'session'

    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.id'))
    expiration_date = db.Column(db.DateTime)

class TransactionHistoryTable(db.Model):

    __tablename__ = 'transaction'

    id = db.Column(db.String, primary_key=True)
    seller_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    buyer_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    cart_id = db.Column(db.String, db.ForeignKey('cart.id'), nullable=False)
    shipping_cost_reais = db.Column(db.Integer)
    shipping_cost_cents = db.Column(db.Integer)
    items_cost_reais = db.Column(db.Integer, nullable=False)
    items_cost_cents = db.Column(db.Integer, nullable=False)
    total_cost_reais = db.Column(db.Integer, nullable=False)
    total_cost_cents = db.Column(db.Integer, nullable=False)
    purchase_date = db.Column(db.String, nullable=False)
