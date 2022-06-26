from src.app import app
from src.exceptions.login_exception import InvalidLoginException
from src.exceptions.user_exception import UsernameNotUniqueException
from src.models.user import User
from src.repositories.item_repo import ItemRepository
from src.exceptions.password_exception import InvalidPasswordException
from flask import jsonify, render_template, request, redirect, url_for
from src.repositories.session_repo import SessionRepository
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

@app.route('/signup', methods=['GET', 'POST'])
def signUp():
   if (request.method == 'GET'):
      return render_template('signup.html', title='Sign Up')
   code = 200
   messages = []
   username = request.form.get('username')
   password = request.form.get('password')
   try:
      newUser = User(username, password)
      UserRepository().insert_user(newUser)
      messages.append('User {} registered! Please log in.'.format(newUser.username))
      return redirect(url_for('login', message=messages))
   except InvalidPasswordException as e:
      code = 422
      messages.append(str(e))
   except UsernameNotUniqueException as e:
      code = 409
      messages.append(str(e))
   except Exception as e:
      code = 500
      messages.append(str(e))
   return render_template('signup.html', messages=messages), code

@app.route('/login', methods=['GET','POST'])
def login():
   messages = [request.args.get('message')] if request.args.get('message') else []
   if (request.method == 'GET'):
      return render_template('login.html', title='Login', messages=messages)
   code = 200
   username = request.form.get('username')
   password = request.form.get('password')
   try:
      session = SessionRepository().get_session_by_credentials(username, password)
      messages.append('Welcome, {}'.format(session.user.username))
      return jsonify({ 'session_id': session.id.hex }), 200
   except InvalidLoginException as e:
      code = 401
      messages.append(str(e))
   except Exception as e:
      code = 500
      messages.append(str(e))
   return render_template('login.html', title='Login', messages=messages), code



