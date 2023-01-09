#!/usr/bin/python3
"""
Replace an element in a list at a specific position without
modifying the original list
"""


def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
