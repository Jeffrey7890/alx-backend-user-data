#!/usr/bin/env python3

""" Personal data for users """

import logging
import mysql.connector  # type: ignore
import os
import re
from typing import List, Tuple

PII_FIELDS = ('password', 'email', 'ssn', 'Name', 'phone')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: Tuple[str, ...]):
        """ Initialization of class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ custom formating with filter_datum function"""
        s = super().format(record)
        s = filter_datum(self.fields, self.REDACTION, s, self.SEPARATOR)
        return (s)


def filter_datum(
        fields: Tuple[str, ...], redaction: str,
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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ connecting to a secure database """

    user = os.getenv('PERSONAL_DATA_DB_USERNAME')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD')
    host = os.getenv('PERSONAL_DATA_DB_HOST')
    if user is None:
        user = 'root'
    if password is None:
        password = ''
    if host is None:
        host = 'localhost'
    mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database='my_db'
            )
    return mydb
