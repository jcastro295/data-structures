'''
selection_sort.py
-----------------

This module contains the selection_sort function, which is an implementation of the selection sort algorithm.
'''


def selection_sort(arr):
    '''
    Sort an array using the selection sort algorithm

    Parameters
    ----------
    arr : list, ndarray
        list of integers to be sorted
    
    Returns
    -------
    list, ndarray
        sorted list of integers
    '''

    for i in range(0, len(arr)-1):
        idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[idx]:
                idx = j
        if idx != i:
            arr[i], arr[idx] = arr[idx], arr[i]

    return arr


if __name__ == '__main__':

    import numpy as np

    # case test
    np.random.seed(42)
    arr = np.random.randint(0, 100, 20)

    print("Original array:", arr)
    print("Sorted array:", selection_sort(arr))
