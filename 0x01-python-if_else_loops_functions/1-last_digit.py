#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if last_digit < 0:
    last_digit = number % -10
else:
    lastdigit = number % 10

if last_digit > 5:
    print("Last digit of {:d}is{:d} and is greaterthan 5".format(number, lastdigit))

elif last_digit < 6 and lastdigit != 0:
    print("Last digit of {:d}is{:d} and is less than 6 and not 0".format(number, lastdigit))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))
