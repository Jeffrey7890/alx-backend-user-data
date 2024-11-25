#!/usr/bin/env python3

""" implementation of basic authentication """


from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ Basic auth, class """
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """ extracts the base64 auth header"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header.startswith('Basic '):
            return authorization_header[len('Basic '):]
        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """ decoding base64 to ascii """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        valid = None
        try:
            valid = base64.b64decode(
                    base64_authorization_header,
                    validate=True)
            decode_str = valid.decode('utf-8')
            return decode_str
        except Exception:
            return valid

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """ get user credentials, (email, password) """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        credentials = decoded_base64_authorization_header.split(':')
        return credentials[0], credentials[1]

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """ get user object from database """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        credential = User.search({'email': user_email})
        if len(credential) == 0:
            return None

        user = credential[0]
        if user.is_valid_password(user_pwd):
            return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        if request is None:
            return None
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None
        base64_auth = self.extract_base64_authorization_header(auth_header)
        if base64_auth is None:
            return None
        decode_auth = self.decode_base64_authorization_header(base64_auth)
        if decode_auth is None:
            return None
        email, pwd = self.extract_user_credentials(decode_auth)
        user = self.user_object_from_credentials(email, pwd)
        if user is None:
            return None
        return user
