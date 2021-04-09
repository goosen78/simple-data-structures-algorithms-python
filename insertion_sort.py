#!/usr/bin/env python3
""" 
Insertion Sort Script

"""

def insertion_sort(L):
    """
    Sorts a list in increasing order. Because of lists are mutable
    this function does not have to return something.
    This algorithm uses insertion sort.
    @param L: a list (in general unsorted)
    """
    # a list of 1 element is a list already sorted
    # so range starts at 1, not at 0. In addition,
    # it goes until len(L) because all elements
    # must be inserted (from 1 to len(L) - 1)
    for i in range(1, len(L)):
        value = L[i]
        hole = i
        
        # the condition hole > 0 should be evaluated
        # first. Otherwise, an exception will be raised.
        # However, in Python L[-1] gives the last element
        # of L, but in other programming languages not.
        # hole = 0 means that value must be placed
        # at the beginning of the list
        # L[hole - 1] means that all the elements to
        # the left including L[hole - 1] are less
        # than value, so value should be placed at L[hole]
        while hole > 0 and L[hole - 1] > value:
            L[hole] = L[hole -1]
            hole -= 1
        
        L[hole] = value        
    


list1 = [1, -2, 3, 2, 0, 4, -1, 2, 0, 1, -5]
#list1 = [2]
insertion_sort(list1)
print(list1)