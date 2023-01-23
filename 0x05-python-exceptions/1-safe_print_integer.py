#!/usr/bin/python3

def safe_print_integer(value):
    """
    Print an integer with "{:d}.format()
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
