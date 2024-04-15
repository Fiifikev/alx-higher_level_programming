#!/usr/bin/python3
"""
Contains an inherited function
"""


def inherits_from(obj, a_class):
    """
    Function thats returns true if inheritance
    is inherited directely or indirectly
    """
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    return False
