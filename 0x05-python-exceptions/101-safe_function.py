#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        solution = fct(*args)
        return solution
    except Exception as std:
        print(f"Exception: {std}", file=stderr)
        return None
