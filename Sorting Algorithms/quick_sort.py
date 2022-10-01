"""
Quick sort is a divide and conquer algorithm
Steps:
1. We first select an element randomly which we call pivot element. We can choose any element as pivot element.
   But for consistency and performce purposes we select middle element of array as the pivot element.
2. Then we move all the elments lower than pivot to the left and higher than pivot to the right to the pivot
3. Then we recursively apply the above 2 steps seperately to each of the sub-arrays of 
   element smaller and larger than last pivot
3. Then we recursively apply the above 2 steps seperately to each of the sub-arrays of 
   element smaller and larger than last pivot
   
   
"""


def partition(array, low, high):

	pivot = array[high]

	i = low - 1

	for j in range(low, high):
		if array[j] <= pivot:

			i = i + 1

			array[i], array[j] = array[j], array[i]

	array[i + 1], array[high] = array[high], array[i + 1]

	return i + 1


def quickSort(array, low, high):
	if low < high:
		pi = partition(array, low, high)

		quickSort(array, low, pi - 1)

		quickSort(array, pi + 1, high)


A= [4,6,2,7,8,3,0]

quickSort(A, 0, len(A)- 1)
print(A)

