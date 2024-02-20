'''
binary_search.py
----------------

This module contains the binary_search function, which is a recursive implementation of the binary search algorithm.
'''


def binary_search(arr, left, right, x):

    while left <= right:

        m = left + (right-left)//2

        # Check if x is present at mid
        if arr[m] == x:
            return m

        # If x greater, ignore left half
        if arr[m] < x:
            left = m + 1
        # If x is smaller, ignore right half
        else:
            right = m - 1

    # If we reach here, then element was not present
    return -1



def binary_search_recursive(array, left, right, x):

    if right >= left:

        mid = left + (right-left)//2

        # if element is present at the middle
        if array[mid] == x:
            return mid

        # search the left half
        if array[mid] > x:
            return binary_search_recursive(array, left, mid-1, x)
        # search the right half
        else:
            return binary_search_recursive(array, mid+1, right, x)

    # element is not present in array
    else:
        return -1


if __name__ == '__main__':
    
    # case test
    array = [-1,0,3,5,9,12]
    x = 9

    print("Binary search:", binary_search(array, 0, len(array), x))
    print("Recursive binary search:", binary_search_recursive(array, 0, len(array), x))
