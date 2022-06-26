from datetime import datetime
from re import L
from src.database.tables import SessionTable
from src.exceptions.session_exception import SessionExpiredException
from src.exceptions.login_exception import InvalidLoginException
from src.models.session import Session
from src.app import db
from src.repositories.user_repo import UserRepository

class SessionRepository:

    def get_session_by_id(self, session_id: str):
        session = db.session.query(SessionTable).filter_by(id=session_id).first()
        if (datetime.today() > session.expiration_date):
            raise SessionExpiredException
        user = UserRepository().get_user_by_id(session.user_id)
        # cart = CartRepository().get_cart(session.cart_id)
        session = Session(user, id=session.id)
        # session.cart = cart
        return session

    def renew_session(self, session_id: str):
        session = db.session.query(SessionTable).filter_by(id=session_id).first()
        if (datetime.today() > session.expiration_date):
            raise SessionExpiredException
        user = UserRepository().get_user_by_id(session.user_id)
        # cart = CartRepository().get_cart(session.cart_id)
        updatedSession = Session(user, id=session.id)
        # updatedSession.cart = cart
        session.expiration_date = updatedSession.expiration_date
        db.session.commit()
        return updatedSession

    def insert_session(self, session: Session):
        newSession = SessionTable(
            id=session.id.hex,
            user_id=session.user.id.hex,
            #cart_id=session.cart.id.hex,
            expiration_date=session.expiration_date
            )
        db.session.add(newSession)
        db.session.commit()

    def get_session_by_credentials(self, username: str, password: str) -> Session:
        user = UserRepository().get_user_by_username(username)
        if ((not user) or (user.password != password)):
            raise InvalidLoginException
        else:
            newSession = Session(user)
            SessionRepository().insert_session(newSession)
            return newSession

    def delete_session_by_id(self, session_id: str):
        session = db.session.query(SessionTable).filter_by(id=session_id).first()
        if session:
            db.session.delete(session)
            db.session.commit()