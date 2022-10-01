class Solution {
	int longestCommonSubsequenceUtil(string text1, string text2, int n, int m) {
		if (n == 0 || m == 0)
			return 0;

		vector<vector<int>>L(n+1, vector<int>(m+1, 0));

		for (int i = 0; i <= n; i++) {
			for (int j = 0; j <= m; j++) {
				if (i == 0 || j == 0)
					L[i][j] = 0;
				else if (text1[i-1] == text2[j-1])
					L[i][j] = 1 + L[i-1][j-1];
				else
					L[i][j] = max(L[i][j-1], L[i-1][j]);
			}
		}

		return L[n][m];
	}

public:
	int longestCommonSubsequence(string text1, string text2) {
		int n = text1.size();
		int m = text2.size();

		return longestCommonSubsequenceUtil(text1, text2, n, m);
	}
};