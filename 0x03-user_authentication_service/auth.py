#!/usr/bin/env python3
""" authorization helper functions """

import bcrypt
from db import DB
from user import User
import uuid
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def create_session(self, email: str) -> str:
        """ create a session id """
        try:
            user = self._db.find_user_by(email=email)
            s_id = self._generate_uuid()
            self._db.update_user(user.id, session_id=s_id)
            return s_id
        except NoResultFound:
            return None

    def valid_login(self, email: str, password: str) -> bool:
        """ validate user login """
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False

    def register_user(self, email: str, password: str) -> User:
        """ registers user in
        database
        """
        try:
            u = self._db.find_user_by(email=email)
            if u is not None:
                raise ValueError(f'{email} already exists')
        except NoResultFound:
            h_pwd = _hash_password(password)
            user = self._db.add_user(email, h_pwd)
            return user

    def _generate_uuid(self):
        """ create a uuid """
        return str(uuid.uuid4())


def _hash_password(password: str) -> bytes:
    """ hashes password
    with bcrypt
    """
    pwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pwd, salt)
    return hashed_password
