#!/usr/bin/python3
"""Defines a peak-finding algorithm"""


def find_peak(list_of_integers):
    """Finds the peaks in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    left = 0
    right = length - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
