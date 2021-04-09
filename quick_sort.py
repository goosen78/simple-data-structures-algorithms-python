#!/usr/bin/env python3
""" 
Quick Sort Script

"""

def quick_sort(L):
    """
    Sorts a list in increasing order. Because of lists are mutable
    this function does not have to return something.
    This algorithm uses quick sort.
    @param L: a list (in general unsorted)
    """
    
    def partition(L):
        """
        Divide a list into two parts one
        the left part where all elements
        are less than the pivot
        and the right part where all elements
        are greater than the pivot
        @param L: a list
        @return: a list with pivot placed
                in its final sorted place
                and all the elements to the left
                less than it, and all the elements
                to the right greater than it.
        """
        # the last element of L is chosen as a pivot
        pivot  = L[-1]
        
        # remember that left_list = right_list 
        # assign the same reference to both variables
        # thus, both are eventually the same list
        left_list = [] 
        right_list = []
        
        for element in L[:-1]:
            if element <= pivot:
                left_list.append(element)
            else:
                right_list.append(element)
        
        # when reaching this point, pivot is
        # in its sorted place
        return left_list, pivot, right_list        
    
    
    
    # an empty list or a list of one element
    # is a list that is already sorted
    if len(L) < 2:
        return L
    
    left, pivot, right = partition(L)
    
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)
    
    return sorted_left + [pivot] + sorted_right



L = list(range(10, 0, -1)) + list(range(20, 0, -1))
print("Before sorting")
print(L)
print("After sorting")
L = quick_sort(L)
print(L)
print("Done")