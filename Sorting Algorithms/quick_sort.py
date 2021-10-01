"""
Quick sort is a divide and conquer algorithm
Steps:
1. We first select an element randomly which we call pivot element. We can choose any element as pivot element.
   But for consistency and performce purposes we select middle element of array as the pivot element.
2. Then we move all the elments lower than pivot to the left and higher than pivot to the right to the pivot
3. Then we recursively apply the above 2 steps seperately to each of the sub-arrays of 
   element smaller and larger than last pivot
"""


def quick_sort(array):
    if len(array) < 2:
        return array
    pivot_element = array[int(len(array)/2)]
    lower_elements = [i for i in array if i < pivot_element]
    higher_elements = [i for i in array if i > pivot_element]
    return quick_sort(lower_elements)+[pivot_element]+quick_sort(higher_elements)


if __name__ == '__main__':
    numer_of_elements = int(input('Enter number of items in array: '))
    array = []
    for i in range(numer_of_elements):
        n = int(input())
        array.append(n)
    sorted_array = quick_sort(array)
    print(f"Unsorted array: {array}")
    print(f"Sorted array: {sorted_array}")
