#!/usr/bin/env python3
""" Encrypting passwords """

import bcrypt


def hash_password(password: str) -> bytes:
    """hashing the password using bcrypt"""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ check is password is valid """
    return (bcrypt.checkpw(password.encode('utf-8'), hashed_password))
