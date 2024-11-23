#!/usr/bin/env python3

""" Personal data for users """

import logging
import re
from typing import List

PII_FIELDS = ('password', 'email', 'ssn', 'Name', 'phone')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initialization of class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ custom formating with filter_datum function"""
        s = super().format(record)
        s = filter_datum(self.fields, self.REDACTION, s, self.SEPARATOR)
        return (s)


def filter_datum(
        fields: List[str], redaction: str,
        message: str, separator: str) -> str:
    """ returns obfuscated log message """
    for f in fields:
        replace = f + "=" + redaction
        message = re.sub(f + "[^{}]*".format(separator), replace, message)
    return (message)


def get_logger() -> logging.Logger:
    """ creates a logger with PIL_FIELDS to redact """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    f = RedactingFormatter(PII_FIELDS)
    ch.setFormatter(f)
    logger.addHandler(ch)
    logger.propagate = False
    return (logger)
