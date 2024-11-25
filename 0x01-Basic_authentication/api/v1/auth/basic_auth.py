#!/usr/bin/env python3

""" implementation of basic authentication """


from api.v1.auth.auth import Auth


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
