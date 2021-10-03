#python heap Sort
 
#function of heapify
#n=size of heap
def heapify(arr, n, i):
    largest = i  #initialize the largest as the root
    l = 2 * i + 1#check child of left = 2*i + 1
    r = 2 * i + 2#check child of right = 2*i + 2
 
    #if left child of root exists and > than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
     #if right child of root exists and > than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    #changing the root to largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        #heapify the root.
        heapify(arr, n, largest)
 
#function heapsort to sort 
def heapSort(arr):
    n = len(arr)
 
    #build the maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    #extracting the elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
 
 
#---main program--
arr = [12, 11, 13, 5, 6, 7]
print("Array we entering: ",arr)
heapSort(arr)
print()
print("Sorted array is",arr)

