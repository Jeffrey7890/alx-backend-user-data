#!/usr/bin/env python3
""" authorization helper functions """

import bcrypt


def _hash_password(password: str) -> bytes:
    """ hashes password
    with bcrypt
    """
    pwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pwd, salt)
    return hashed_password
