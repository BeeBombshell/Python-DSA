
class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        L, B = len(N), 1
        while B:
            B = 0
            for i in range(L-1):
                if N[i] > N[i+1]: N[i], N[i+1], B = N[i+1], N[i], 1
        return N
		