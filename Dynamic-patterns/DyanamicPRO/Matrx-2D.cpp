class Solution {
public:
	vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int K) {


		int m = mat.size();
		int n = mat[0].size();

		vector<vector<int>>sum(m+1, vector<int>(n+1, 0));
		for (int i = 1; i <= m; i++) {
			for (int j = 1; j <= n; j++) {
				sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + mat[i-1][j-1];
			}
		}

		vector<vector<int>>res(m, vector<int>(n, 0));
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				int r1 = max(0, i-K); int c1 = max(0, j-K);
				int r2 = min(m-1, i+K); int c2 = min(n-1, j+K);
				r1++; r2++;
				c1++; c2++;
				res[i][j] = sum[r2][c2] - (sum[r2][c1-1] + sum[r1-1][c2]- sum[r1-1][c1-1]);
			}
		}

		return res;
	}
};