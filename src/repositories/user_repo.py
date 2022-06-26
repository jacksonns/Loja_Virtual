from re import T
from sqlalchemy import exc
from src.database.tables import UserTable
from src.exceptions.user_exception import UsernameNotUniqueException
from src.models.user import User
from src.app import db

class UserRepository:

    def get_user_by_id(self, user_id):
        user = db.session.query(UserTable).filter_by(id=user_id).first()
        return User(user.username, user.password, (user.budget_reais, user.budget_cents), id=user.id) if user else None

    def get_user_by_username(self, username):
        user = db.session.query(UserTable).filter_by(username=username).first()
        return User(user.username, user.password, (user.budget_reais, user.budget_cents), id=user.id) if user else None

    def insert_user(self, user: User):
        try:
            newUser = UserTable(
                id=user.id.hex,
                username=user.username,
                password=user.password,
                budget_reais=0,
                budget_cents=0
                )
            db.session.add(newUser)
            db.session.commit()
        except exc.IntegrityError:
            raise UsernameNotUniqueException(user.username)
        