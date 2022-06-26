from src.app import app
from src.models.user import User
from src.repositories.item_repo import ItemRepository
from src.exceptions.password_exception import InvalidPasswordException
from flask import render_template, request

from src.repositories.user_repo import UserRepository

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

@app.route('/signup', methods=['POST'])
def signUp():
   code = 200
   messages = []
   username = request.form.get('username')
   password = request.form.get('password')
   try:
      newUser = User(username, password)
      UserRepository().insert_user(newUser)
      messages.append('Usuário cadastrado!')
   except InvalidPasswordException as e:
      code = 422
      messages.append(str(e))
   except Exception as e:
      code = 500
      messages.append(str(e))
   return render_template('base.html', messages=messages), code



