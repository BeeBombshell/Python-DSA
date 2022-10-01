class Solution {
public:
	int findTargetSumWays(vector<int>& nums, int S) {
		int n = nums.size();
		unordered_map<int, int>hm;

		hm[0] = 1;
		for (int i = 0; i < n; i++) {
			auto mp = hm;
			hm.clear();

			for (auto it = mp.begin(); it != mp.end(); it++) {
				hm[it->first + nums[i]] += it->second;
				hm[it->first - nums[i]] += it->second;

			}
		}

		return hm[S];
	}
};