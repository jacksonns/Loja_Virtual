from src.app import app
from src.repositories.item_repo import ItemRepository

from flask import render_template

import jsonpickle

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