#!/usr/bin/python3
"""
This is one inheritance function
"""


def lookup(obj):
    """Function that returns the list of available
    variables
    """
    return [attr for attr in dir(obj)]
