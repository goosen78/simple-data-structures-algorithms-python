#!/usr/bin/env python3
""" 
Binary Search Script

"""


def binary_search_iterative(lst, value):
    """
    Searches for an value within a given list.
    This algorithm uses binary search in an iterative way.

    @param lst: a list containing numbers
    @param value: value to be found

    @return: True if the value has been found. Otherwise, False.
    """
    if len(lst) == 0:
        return False

    # if high = len(lst) you will get an error
    # when the element is higher than the last element
    # of a sorted list, and you will have to make more
    # complicated the condition in the while loop.
    high = len(lst) - 1
    low = 0

    while high >= low:
        middle = (high + low) // 2
        if lst[middle] == value:
            return True
        elif lst[middle] > value:
            high = middle - 1
        else:
            low = middle + 1

    # if value not found
    return False

def binary_search_recursive(lst, value):
    """
    Searches for an value within a given list.
    This algorithm uses binary search in a recursive way.

    @param lst: a list containing numbers
    @param value: value to be found

    @return: True if the value has been found. Otherwise, False.
    """
    if len(lst) == 0:
        return False

    middle = len(lst) // 2

    if lst[middle] == value:
        return True
    elif lst[middle] > value:
        return binary_search_recursive(lst[:middle], value)
    else:
        return binary_search_recursive(lst[middle + 1:], value)
