#!/usr/bin/env python3
""" authorization helper functions """

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

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


def _hash_password(password: str) -> bytes:
    """ hashes password
    with bcrypt
    """
    pwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pwd, salt)
    return hashed_password