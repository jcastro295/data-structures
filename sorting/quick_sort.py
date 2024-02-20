'''

quick_sort.py
-------------

This module contains the quick_sort function, which is an implementation of the quick sort algorithm.
'''


def partition(array, left, right):
    '''
    Function to partition the array on the basis of pivot element;
    all elements smaller than pivot are on the left and greater on the right

    Parameters
    ----------
    array : list, ndarray
        list of integers to be sorted
    left : int
        left index of the array
    right : int
        right index of the array

    Returns
    -------
    int
        position from where partition is done
    '''

    # Choose the rightmost element as pivot
    pivot = array[right]

    # Pointer for greater element
    i = left - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(left, right):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with
    # e greater element specified by i
    (array[i + 1], array[right]) = (array[right], array[i + 1])

    # Return the position from where partition is done
    return i + 1


def quick_sort(array, left, right):
    '''
    Sort an array using the quick sort algorithm

    Parameters
    ----------

    array : list, ndarray
        list of integers to be sorted
    left : int
        left index of the array
    right : int
        right index of the array
    
    Returns
    -------
    None
    '''

    if left < right:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, left, right)

        # Recursive call on the left of pivot
        quick_sort(array, left, pi - 1)

        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, right)


if __name__ == '__main__':

    import numpy as np

    # case test
    np.random.seed(42)
    arr = np.random.randint(0, 100, 20)

    print("Original array:", arr)
    quick_sort(arr, 0, len(arr)-1)
    print("Sorted array:", arr)
