'''

bubble_sort.py
--------------

This module contains the bubble_sort function, which is an implementation of the bubble sort algorithm.
'''

def bubble_sort(arr):
    '''
    Sort an array using the bubble sort algorithm

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
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


if __name__ == '__main__':

    import numpy as np

    # case test
    np.random.seed(42)
    arr = np.random.randint(0, 100, 20)

    print("Original array:", arr)
    print("Sorted array:", bubble_sort(arr))