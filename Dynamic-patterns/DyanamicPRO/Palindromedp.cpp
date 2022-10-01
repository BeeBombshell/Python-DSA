class Solution {
public:
	int minCut(string s) {

		int n = s.length();

		int res[n];
		bool P[n][n];

		for (int i = 0; i < n; i++)
			P[i][i] = true;


		for (int L = 2; L <= n; L++) {
			for (int i = 0; i < n-L+1; i++) {
				int j = i+L-1;

				if (L == 2) {
					P[i][j] = (s[i] == s[j]);
				} else {
					P[i][j] = (s[i] == s[j]) && P[i+1][j-1];
				}
			}
		}

		for (int i = 0; i < n; i++) {
			if (P[0][i])
				res[i] = 0;
			else {
				res[i] = INT_MAX;
				for (int j = 0; j < i; j++) {
					if (P[j+1][i] && res[i] > 1 + res[j])
						res[i] = 1+res[j];
				}
			}
		}

		return res[n-1] == INT_MAX ? 1 : res[n-1];
	}
};