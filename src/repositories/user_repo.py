from src.database.tables import UserTable
from src.models.user import User
from src.app import db

from src.exceptions.user_exception import InvalidUserException

class UserRepository:

    def get_user_by_id(self, user_id: str):
        user = db.session.query(UserTable).filter_by(id=user_id).first()
        if not user: raise InvalidUserException()
        return User(user.username, user.password, (user.budget_reais, user.budget_cents))
    
    def get_user_id_by_username(self, username: str):
        user = db.session.query(UserTable).filter_by(username=username).first()
        if not user: raise InvalidUserException()
        return user.id