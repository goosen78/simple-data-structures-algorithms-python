#!/usr/bin/env python3
""" 
Linear Search Script

"""

def linear_search(lst, value):
    """
    Searches for a specified value in a list.
    It performs linear search in an iterative way.

    @param lst: a list containing numbers
    @param value: value to search

    @return: True if value is found. Otherwise, False.
    """
    for element in lst:
        if element == value:
            return True

    # if value has not been found
    return False

def linear_search_recursive(lst, value):
    """
    Searches for a specified value in a list.
    It performs linear search in a recursive way.

    @param lst: a list containing numbers
    @param value: value to search

    @return: True if value is found. Otherwise, False.
    """
    if len(lst) == 0:
        return False

    if lst[0] == value:
        return True

    return linear_search_recursive(lst[1:], value)

def linear_search_v2(lst, value):
    """
    Searches for a specified value in a list.

    @param lst: a list containing numbers
    @param value: value to be search

    @return: True if value is found. Otherwise, False.
    """
    for i in range(len(lst)):
        if lst[i] == value:
            return True

    # if value has not been found
    return False
