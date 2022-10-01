


class Solution {
public:
	bool PredictTheWinner(vector<int>& nums) {
		int n = nums.size();

		int res[n][n];

		for (int i = 0; i < n; i++)
			res[i][i] = nums[i];

		for (int l = 2; l <= n; l++) {
			for (int i = 0; i+l-1 < n; i++) {
				int j = i+l-1;
				int a = (i+1 <= j-1) ? res[i+1][j-1] : 0;
				int b = (i+2 <= j) ? res[i+2][j] : 0;
				int c = (i <= j-2) ? res[i][j-2] : 0;

				res[i][j] = max(nums[i] + min(a,b), nums[j] + min(a, c));
			}
		}

		int total = 0;
		for (int i = 0; i < n; i++)
			total += nums[i];

		return res[0][n-1] >= total - res[0][n-1];
	}
};