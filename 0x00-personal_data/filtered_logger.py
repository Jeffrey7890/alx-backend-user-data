#!/usr/bin/env python3

""" Personal data for users """

import re


def filter_datum(fields, redaction, message, separator) -> str:
    """ returns obfuscated log message """
    for f in fields:
        replace = f + "=" + redaction
        message = re.sub(f + "[^{}]*".format(separator), replace, message)
    return (message)
