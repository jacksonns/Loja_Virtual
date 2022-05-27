from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    
    __tablename__ = 'user'

    username = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    budget_reais = Column(Integer, nullable=False)
    budget_cents = Column(Integer, nullable=False)


class Item(Base):

    __tablename__ = 'item'

    item_id = Column(String, primary_key=True)
    seller = Column(String, ForeignKey('user.username'))
    name: Column(String, nullable=False)
    description: Column(String, nullable=False)
    price_reais = Column(Integer, nullable=False)
    price_cents = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    sale = Column(Integer) 


class Session(Base):

    __tablename__ = 'session'

    session_id = Column(Integer, primary_key=True)
    username = Column(String, ForeignKey('user.username'))
    expiration_date = Column(String)


class Cart(Base):

    __tablename__ = 'cart'

    cart_id = Column(Integer, primary_key=True)
    session_id = Column(String, ForeignKey('session.session_id'))
    item_id = Column(String, ForeignKey('item.item_id'))
    quantity = Column(Integer, nullable=False)