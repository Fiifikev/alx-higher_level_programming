#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    result = 0
    for number in range(x):
        try:
            print("{:d}".format(my_list[number]), end="")
            result += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (result)
