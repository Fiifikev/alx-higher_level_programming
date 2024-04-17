#!/usr/bin/python3
"""writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """ Writes a string to a text file"""
    with open(filename, "w") as f:
        message = f.write(text)
        return message
