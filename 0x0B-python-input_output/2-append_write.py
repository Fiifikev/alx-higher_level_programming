#!/usr/bin/python3
"""appends a string at the end of a text file(UTF8)
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, "a") as f:
        message = f.write(text)
        return message
