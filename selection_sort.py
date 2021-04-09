#!/usr/bin/env python3
""" 
Selection Sort Script

"""

def selection_sort_iterative(L):
    """
    Sorts a list in increasing order. Because of lists are mutable
    this function does not have to return something.
    This algorithm uses selection sort.
    @param L: a list (in general unsorted)
    """
    
    for i in range(len(L) - 1):
        min_index = i
        
        for j in range(i + 1, len(L)):
            if L[min_index] > L[j]:
                min_index = j
        
        # swap only if min_index is not
        # equal to dummy_i, i.e., it has changed
        # in he previous loop
        if min_index != i:
            L[i], L[min_index] = L[min_index], L[i]            

list1 = [1, -2, 3, 2, 0, 4, -1, 2, 5, -5]
#list1 = [2]
selection_sort_iterative(list1)
print(list1)