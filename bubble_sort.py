#!/usr/bin/env python3
""" 
Bubble Sort Script

"""

    
def bubble_sort(L):
    """
    Sorts a list in increasing order. Because of lists are mutable
    this function does not have to return something.
    This algorithm uses bubble sort.
    @param L: a list (in general unsorted)
    """
    for i in range(len(L) - 1):
        already_sorted = True
        for j in range(len(L) - i - 1):
            if L[j] > L[j + 1]:
                already_sorted = False                                
                L[j],  L[j + 1]= L[j + 1], L[j]
        # if no swaps were developed in the previous loop,
        # it means that the list is already sorted. Thus,
        # loop is exited and function terminates (returns None)
        if already_sorted:
            break



list1 = [1, -2, 3, 2, 0, 4, -1, 2, 0, 1, -5, 5, -6]

#list1 = [2, 1, -1]
bubble_sort(list1)
print(list1)