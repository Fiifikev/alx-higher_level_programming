#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    for eachitem in range(len(my_list)):
        if eachitem != idx:
            new_list.append(my_list[eachitem])
    return new_list
