'''
insertion_sort.py
-----------------

This module contains the insertion_sort function, which is an implementation of the insertion sort algorithm.

'''

def insertion_sort(arr):
    '''
    Sort an array using the insertion sort algorithm

    Parameters
    ----------
    arr : list, ndarray
        list of integers to be sorted
    
    Returns
    -------
    list, ndarray
        sorted list of integers
    '''

    for i in range(1, len(arr)):
        cnt, aux = 0, arr[i]
        for j in range(i-1, -2, -1):
            cnt = j
            if arr[j] > aux:
                arr[j+1] = arr[j]
            else:
                break
        arr[cnt+1] = aux

    return arr


if __name__ == '__main__':

    import numpy as np

    # case test
    np.random.seed(42)
    arr = np.random.randint(0, 100, 20)

    print("Original array:", arr)
    print("Sorted array:", insertion_sort(arr))