#!/usr/bin/env python3

""" implementation of basic authentication """


from api.v1.auth.auth import Auth
import base64


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
        except Exception:
            return None
        decode_str = valid.decode('utf-8')
        return decode_str

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
