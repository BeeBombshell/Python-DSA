class Solution {
public:
	int coinChange(vector<int>& coins, int amount) {

		int n = coins.size();
		if (n == 0) return 0;

		vector<int>res(amount+1, INT_MAX);

		res[0] = 0;

		for (int i = 0; i < n; i++) {
			for (int j =  coins[i]; j <= amount; j++) {
				if (res[j-coins[i]] != INT_MAX)
					res[j] = min(res[j], 1+res[j-coins[i]]);
			}
		}

		return res[amount] != INT_MAX ? res[amount] : -1;
	}
};