#!/usr/bin/python3

def magic_calculation(a, b):
    calc = 0
    for num in range(1, 3):
        try:
            if num > a:
                raise Exception("Too far")
            else:
                calc += pow(a, b) / num
        except Exception:
            calc = a + b
            break
    return calc
