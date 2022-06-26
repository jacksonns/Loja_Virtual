from src.database.tables import UserTable
from src.models.user import User
from src.app import db

class UserRepository:

    def get_user_by_id(self, user_id):
        user = db.session.query(UserTable).filter_by(id=user_id).first()
        return User(user.username, user.password, (user.budget_reais, user.budget_cents))

    def get_user_by_username(self, username):
        user = db.session.query(UserTable).filter_by(username=username).first()
        return User(user.username, user.password, (user.budget_reais, user.budget_cents))

    def insert_user(self, user: User):
        newUser = UserTable(
            id=user.id.hex,
            username=user.username,
            password=user.password,
            budget_reais=0,
            budget_cents=0
            )
        db.session.add(newUser)
        db.session.commit()