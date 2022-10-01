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
        