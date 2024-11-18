#!/usr/bin/env python3

""" Personal data for users """

import re


def filter_datum(fields, redaction, message, separator):
    """ returns obfuscated log message """
    for f in fields:
        replace = f + "=" + redaction
        f += "[^{}]*".format(separator)
        message = re.sub(f, replace, message)
    return (message)
