#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    result = 0
    for number in range(x):
        try:
            print("{}".format(my_list[number]), end="")
            result += 1
        except IndexError:
            break
    print("")
    return (result)
