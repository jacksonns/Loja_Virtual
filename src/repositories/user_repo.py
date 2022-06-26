from re import T
from sqlalchemy import exc
import sqlite3
from src.database.tables import UserTable
from src.exceptions.user_exception import UsernameNotUniqueException
from src.models.user import User
from src.app import db

from src.exceptions.user_exception import InvalidUserException

class UserRepository:

    def get_user_by_id(self, user_id: str):
        user = db.session.query(UserTable).filter_by(id=user_id).first()
        if not user: raise InvalidUserException()
        return User(user.username, user.password, (user.budget_reais, user.budget_cents))

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
        except (exc.IntegrityError, sqlite3.IntegrityError):
            db.session.rollback()
            raise UsernameNotUniqueException(user.username)

    def delete_user_by_username(self, username: str):
        user = db.session.query(UserTable).filter_by(username=username).first()
        if user:
            db.session.delete(user)
            db.session.commit()

    def get_user_id_by_username(self, username: str):
        user = db.session.query(UserTable).filter_by(username=username).first()
        if not user: raise InvalidUserException()
        return user.id