'''

heap_sort.py
------------

This module contains the heap_sort function, which is an implementation of the heap sort algorithm.
'''

def heapify(arr, n, idx):
    '''
    To heapify subtree rooted at index i.

    Parameters
    ----------
    arr : list, ndarray
        list of integers to be sorted
    n : int
        size of the heap
    idx : int
        index of the root of the subtree to be heapified
    
    Returns
    -------
    None
    '''

    largest = idx # Initialize largest as root
    left = 2 * idx + 1 # left = 2*i + 1
    right = 2 * idx + 2 # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if left < n and arr[largest] < arr[left]:
        largest = left

    # See if right child of root exists and is
    # greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx] # swap

        # Heapify the root.
        heapify(arr, n, largest)


def heap_sort(arr):
    '''
    Sort an array using the heap sort algorithm

    Parameters
    ----------
    arr : list, ndarray
        list of integers to be sorted
    
    Returns
    -------
    None
    '''

    n = len(arr)

    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)


if __name__ == '__main__':

    import numpy as np

    # case test
    np.random.seed(42)
    arr = np.random.randint(0, 100, 20)

    print("Original array:", arr)
    heap_sort(arr)
    print("Sorted array:", arr)