from src.app import app
from src.models.item import Item
from src.repositories.user_repo import UserRepository
from src.repositories.item_repo import ItemRepository

import uuid
from flask import render_template, request

@app.route('/')
@app.route('/home')
def home():
   return render_template("base.html")

@app.route('/items')
def items():
   items = ItemRepository().get_all_items()
   return render_template('items.html', items_list=items)

@app.route('/items/<id>')
def item(id):
   item = ItemRepository().get_item_by_id(id)
   return render_template('items.html', items_list=[item])

@app.route('/sell', methods=['GET', 'POST'])
def sell():
   if request.method == 'POST':
      data = request.form
      try:
         user = UserRepository().get_user_by_id(data['seller_id'])
         item = Item(str(uuid.uuid4()), user,
                     data['name'], data['description'], 
                     (int(data['price_reais']), int(data['price_cents'])), 
                     int(data['stock']), int(data['sale']) )
         ItemRepository().add_item(item)
      except:
         return 'An error occurred'
      return 'Submitted {}!'.format(data['name'])
   return render_template('sell.html')

@app.route('/cart', methods=['GET', 'POST'])
def cart():
   #to be implemented
   pass

@app.route('/cart/item', methods=['POST', 'DELETE'])
def cart_item():
   #to be implemented
   pass