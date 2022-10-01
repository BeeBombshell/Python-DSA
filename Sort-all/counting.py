class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        C, m, M, S = collections.Counter(N), min(N), max(N), []
        for n in range(m,M+1): S.extend([n]*C[n])
        return S
		