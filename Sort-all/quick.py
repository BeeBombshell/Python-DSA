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
		
		