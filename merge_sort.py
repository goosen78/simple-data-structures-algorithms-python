#!/usr/bin/env python3
""" 
Merge Sort Script

"""

def merge_sort(L):
    """
    Sorts a list in increasing order. 
    This algorithm uses merge sort.
    @param L: a list (in general unsorted)
    @return: a reference containing an ascending order
             sorted version of L
    """
    
    def merge_lists(L1, L2):
        """
        Merge two sorted list in a new sorted list which
        length is len(L1) + len(L2)
        @param L1: a sorted list
        @param L2: a sorted list
        @return: result of merging L1 and L2
        """        
        # list containing L1 and L2 merged and sorted
        merged_list = []
        
        i = j = 0
        
        # repeat while i or j is less than len(L1)
        # and len(L2) respectively, 
        # i.e., until one of two list have been
        # completed added to merged list
        while (i < len(L1) and j < len(L2)):             
            # compare index i (L1) and index j (L2)
            # and add smaller element of the comparison
            if L2[j] < L1[i]:
                merged_list.append(L2[j])
                # increase j by 1 (i.e., go to the next
                # element of L2)
                j += 1
            else:
                merged_list.append(L1[i])
                # increase i by 1 (i.e., go to the next
                # element of L1)
                i += 1                      
        
        # at this point one of the elements of one list has
        # been completed added, while the other list need to
        # add its remaining elements.
        if i < len(L1):
            # if elements of L1 have not been completely added
            # add the remaining, but sorted elements, to the merged list
            merged_list += L1[i:]
        # being here means that all elements of L1 have been added,
        # but not all elements of L2, so they should be added
        # at the end of merged_list. Again, remaining elements of
        # L2 are already sorted.
        else:
            merged_list += L2[j:]
        
        # pass reference of merged_list to L
        return merged_list
                
        
    # check if the list contains no elements or just one
    # i.e. list is already sorted
    if len(L) < 2:        
        return L    
    
    # divide L in two smaller lists
    L1 = L[:len(L) // 2]
    L2 = L[len(L) // 2:]
    
    # sort first half of L (i.e. L1)
    L1 = merge_sort(L1)
    # sort second half of L (i.e. L2)
    L2 = merge_sort(L2)
    
    # merge sorted lists (L1 and L2) in L
    return merge_lists(L1, L2)


L = list(range(10, 0, -1)) + list(range(20, 0, -1))
print("Before sorting")
print(L)
print("After sorting")
L = merge_sort(L)
print(L)