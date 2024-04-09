#!/usr/bin/python3
"""Define a class"""


class LockedClass:
    """
    Prevent the user from instantiating ne LockedClass attributes
    for anything but attributes clled 'first_name'
    """
    __slots__ = ["first_name"]
