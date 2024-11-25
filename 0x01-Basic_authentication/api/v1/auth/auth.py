#!/usr/bin/env python3

""" authorization implementation """

from flask import request
from typing import List, TypeVar


class Auth():
    """ Authorization class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ requiree aithorization """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for p in excluded_paths:
            if path in p:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorize request header """
        if request is None:
            return None
        auth_header = request.headers.get("Authorization")

        if auth_header is None:
            return None
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns current user """
        return None
