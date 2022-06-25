from src.app import app
from src.repositories.item_repo import ItemRepository

from flask import render_template

@app.route('/')
@app.route('/home')
def home():
   return render_template("home.html")

@app.route('/items')
def items():
   items = ItemRepository().get_all_items()
   return render_template('items.html', items_list=items)