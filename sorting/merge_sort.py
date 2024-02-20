'''

merge_sort.py
-------------

This module contains the merge_sort function, which is an implementation of the merge sort algorithm.
'''


def merge(arr, left, mid, right):
	'''
    Merge two subarrays of arr

    Parameters
    ----------
    arr : list, ndarray
        list of integers to be sorted
    left : int
        left index of the array
    mid : int
        middle index of the array
    right : int
        right index of the array
    
    Returns
    -------
    None
    '''

	n1 = mid - left + 1
	n2 = right - mid

	# create temp arrays
	left_arr = [0] * (n1)
	right_arr = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		left_arr[i] = arr[left + i]

	for j in range(0, n2):
		right_arr[j] = arr[mid + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	     # Initial index of first subarray
	j = 0	     # Initial index of second subarray
	k = left	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if left_arr[i] <= right_arr[j]:
			arr[k] = left_arr[i]
			i += 1
		else:
			arr[k] = right_arr[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = left_arr[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = right_arr[j]
		j += 1
		k += 1


def merge_sort(arr, left, right):
	'''
	Sort an array using the merge sort algorithm
	
	Parameters
	----------
	arr : list, ndarray
        list of integers to be sorted
    left : int
        left index of the array
    right : int
        right index of the array
	
	Returns
	-------
	list, ndarray
        sorted list of integers
	'''

	if left < right:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		mid = left + (right - left)//2

		# Sort first and second halves
		merge_sort(arr, left, mid)
		merge_sort(arr, mid+1, right)
		merge(arr, left, mid, right)


if __name__ == '__main__':

    import numpy as np

    # case test
    np.random.seed(42)
    arr = np.random.randint(0, 100, 20)

    print("Original array:", arr)
    merge_sort(arr, 0, len(arr)-1)
    print("Sorted array:", arr)
