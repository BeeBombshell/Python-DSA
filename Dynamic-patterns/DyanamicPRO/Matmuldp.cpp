class Solution {
public:
	int minScoreTriangulation(vector<int>& A) {

		int n = A.size();        
		vector<vector<int>>dp(n, vector<int>(n, 0));

		for (int L = 2; L <= n; L++) {
			for (int i = 0; i+L < n; i++) {
				int j = i+L;
				dp[i][j] = INT_MAX;
				for (int k = i+1; k < j; k++) {
					dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i]*A[k]*A[j]);
				}
			}
		}

		return dp[0][n-1];
	}
};
