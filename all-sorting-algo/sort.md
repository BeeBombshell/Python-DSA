### Sorting Algorithms:

# Selection Sort
# Bubble Sort
# Insertion Sort
# Binary Insertion Sort
# Counting Sort
# QuickSort
# Merge Sort
# Bucket Sort
## Selection Sort:
#This program sorts the list by finding the minimum of the list, removing it from the original list, and appending it onto the output list. As it finds the minumum during each iteration, the length of the original list gets shorter by one and the length of the output list gets longer by one. This program uses the min function with a lambda function to find the index of the minimum value in the unsorted list. The output list is created using a list comprehension. This algorithm is O(n²). It is able to sort 8 out of 10 test cases but exceeds the time limit on the ninth test case.


class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        L = len(N)
        return [N.pop(min(range(L-i), key = lambda x: N[x])) for i in range(L)]



		
## Bubble Sort:
# This program sorts the list by looping through the original list and finding any adjacent pairs of numbers that are out of order. If it finds such a pair, it switches their locations. It continues to check for adjacent pairs that are out of order until it has completed the pass through the list. If it finds a pair, it will set B = 1 which tells the program to pass through the list again and continue switching adjacent values that are out of order. If it can make it through the list without finding any adjacent pairs that are out of order, we can conclude that the list is sorted. The value of B will stay 0 and the outer while loop will end. This algorithm is O(n²). It is able to sort 8 out of 10 test cases but exceeds the time limit on the ninth test case.


class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        L, B = len(N), 1
        while B:
            B = 0
            for i in range(L-1):
                if N[i] > N[i+1]: N[i], N[i+1], B = N[i+1], N[i], 1
        return N
		
		
## Insertion Sort:
# This program sorts the list by sequentially inserting each element into the proper location within the sorted front portion of the original list. It starts by inserting the second number into the proper location within the first two numbers. It then inserts the third number into the proper location within the first three numbers. After each iteration, the front portion of the list (i.e. the sorted portion) will grow in length by 1. A number is removed from the back portion of the list (i.e. the unsorted portion) and placed into the appropriate location in the sorted portion of the list. Once we place the last number into the correct location within the sorted numbers, the entire list will have become sorted. This algorithm is O(n²). It is able to sort 9 out of 10 test cases but exceeds the time limit on the last test case.

class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        L = len(N)
        for i in range(1,L):
            for j in range(0,i):
                if N[i] < N[j]:
                    N.insert(j, N.pop(i))
                    break
        return N		
		
		
## Binary Insertion Sort: (944 ms) (beats ~6%)
# This program sorts the list by sequentially inserting each element into the proper location within the sorted front portion of the original list. It starts by inserting the second number into the proper location within the first two numbers. It then inserts the third number into the proper location within the first three numbers. After each iteration, the front portion of the list (i.e. the sorted portion) will grow in length by 1. A number is removed from the back portion of the list (i.e. the unsorted portion) and placed into the appropriate location in the sorted portion of the list. Once we place the last number into the correct location within the sorted numbers, the entire list will have become sorted. This algorithm is still O(n²). It is not O(n log n) despite using a binary search because the insertion step is time consuming. The advantage of the binary insertion sort versus the generic insertion sort is that this one does a binary search which is O(log i) (for the ith iteration) while the generic one does a linear search which is O(i) (for the ith iteration). Because of this improvement, this program is able to sort all 10 cases although it is not a very fast approach compared to some of the other algorithms.
class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        L = len(N)
        for i in range(1,L): bisect.insort_left(N, N.pop(i), 0, i)
        return N
		
		
## Counting Sort: (136 ms) (beats ~97%)
# This program starts by creating a dictionary of key-value pairs that records the total count of each element of the original list. The minimum and maximum value of the list is also found. The program then loops through every integer between the min and max value (in order) and appends that number to the output list based on its count within the original list. For example, if the number 3 occurs 4 times in the original list, then the output list will be extended by [3,3,3,3]. The output will be the sorted form of the original list as it consists of an ordered list of the numbers in the original list. This approach is a linear time sorting algorithm that sorts in O(n+k) time, where n is the number of elements and k is the statistical range of the dataset (i.e. max(N) - min(N)). It is able to sort all test cases in only 136 ms.
class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        C, m, M, S = collections.Counter(N), min(N), max(N), []
        for n in range(m,M+1): S.extend([n]*C[n])
        return S
		
		
## QuickSort: (316 ms) (beats ~54%)
# This program uses a recursive Divide and Conquer approach to sort the original list. The recursive function quicksort is called on the original list. A partition subroutine then takes the input and pivots around the median position's value (pivot value). Specifically, it uses swaps to place numbers less than the pivot value to the left of the pivot index and numbers greater than the pivot value to the right of the pivot index. At the end of the partition subroutine, we are left with the situation that the value at the pivot index is located at what will be its final position in the sorted output. We then do a quicksort on these left and right halves and continue this rescursively until we get a list of length 1 which is already sorted. Once all of the quicksort subroutines are completed, the entire list is in sorted order and the initial quicksort call completes and we can return the sorted list. In the average case, this method is O(n log n). In the worst case, however, it is O(n²). It is able to sort all test cases in 316 ms.
class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        def quicksort(A, I, J):
            if J - I <= 1: return
            p = partition(A, I, J)
            quicksort(A, I, p), quicksort(A, p + 1, J)
        
        def partition(A, I, J):
            A[J-1], A[(I + J - 1)//2], i = A[(I + J - 1)//2], A[J-1], I
            for j in range(I,J):
                if A[j] < A[J-1]: A[i], A[j], i = A[j], A[i], i + 1
            A[J-1], A[i] = A[i], A[J-1]
            return i
        
        quicksort(N,0,len(N))
        return N
		
		
## Merge Sort: (324 ms) (beats ~51%)
# This program uses a recursive Divide and Conquer approach to sort the original list. The recursive function mergesort is called on the original list. The function divides the list into two halves (a left half and a right half) and calls the mergesort routine recursively on each of them. Once each half is sorted, the merge subroutine merges the two lists into one list by appending the lower number from the front of each half into the output list S. If one list is exhausted before the other, the remaining list is appended onto S before S is returned. The mergesort function recursively calls on lists that are half the size of the previous list until their length is 1. Such a list is trivially sorted and that list can be returned for merge to join with another list. Eventually all the small lists are merged back into larger lists until the final sorted version of the original list is formed. This method is O(n log n). It is able to sort all test cases in 324 ms.
class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        def mergesort(A):
            LA = len(A)
            if LA == 1: return A
            LH, RH = mergesort(A[:LA//2]), mergesort(A[LA//2:])
            return merge(LH,RH)

        def merge(LH, RH):
            LLH, LRH = len(LH), len(RH)
            S, i, j = [], 0, 0
            while i < LLH and j < LRH:
                if LH[i] <= RH[j]: i, _ = i + 1, S.append(LH[i])
                else: j, _ = j + 1, S.append(RH[j])
            return S + (RH[j:] if i == LLH else LH[i:])
        
        return mergesort(N)		
		
		
## Bucket Sort: (196 ms) (beats ~78%)
# This program sorts the original list by dividing the numbers in the list into 1000 non-overlapping adjacent buckets. The bucketsort function finds the statistical range of the numbers in the original list (i.e. R = max(N) - min(N)) to help map each number into the appropriate bucket. The insertion_sort subroutine is then used to sort the numbers in each of these buckets. The sorted adjacent buckets are then appended onto the output list S which is the sorted version of the original list. This method is O(n²) in the worst case and O(n) on average. The large number of buckets (1000 buckets) was chosen to decrease the time needed to sort the final test case. If too few buckets are used, the time limit gets exceeded for the final test case. It is able to sort all test cases in 196 s.
class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        def insertion_sort(A):
            for i in range(1,len(A)):
                for j in range(0,i):
                    if A[i] < A[j]:
                        A.insert(j, A.pop(i))
                        break
            return A
        
        def bucketsort(A):
            buckets, m, S = [[] for _ in range(1000)], min(A), []
            R = max(A) - m
            if R == 0: return A
            for a in A: buckets[999*(a-m)//R]
            for b in buckets: S.extend(insertion_sort(b))
            return S
    
        return bucketsort(N)
        
		
		