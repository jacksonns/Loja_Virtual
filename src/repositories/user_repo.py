from src.database.tables import UserTable
from src.models.user import User
from src.app import db

class UserRepository:

    def get_user_by_id(self, user_id):
        user = db.session.query(UserTable).filter_by(id=user_id).first()
        return User(user.username, user.password, (user.budget_reais, user.budget_cents))