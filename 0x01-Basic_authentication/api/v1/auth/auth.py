#!/usr/bin/env python3

""" authorization implementation """

from Flask import request
from Typing import List, TypeVar


class Auth():
    """ Authorization class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ requiree aithorization """
        return False

    def authorization_header(self, request=None) -> str:
        """ authorize request header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns current user """
        return None
