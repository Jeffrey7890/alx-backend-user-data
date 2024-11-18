#!/usr/bin/env python3

""" Personal data for users """

import re
from typing import List


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str) -> str:
    """ returns obfuscated log message """
    for f in fields:
        replace = f + "=" + redaction
        message = re.sub(f + "[^{}]*".format(separator), replace, message)
    return (message)
