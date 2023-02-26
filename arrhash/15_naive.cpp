class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // [-1,0,1,2,-1,-4] -> [-4,-1,-1,0,1,2]
        // -4 -> target 4 -> {5:-1, }
        // -1 -> target 1 -> {2:-1, 1:0} -> <-1, 0, 1>
        vector<vector<int>> results;
        // set<vector<int>> results;

        sort(nums.begin(), nums.end());

        int prev = nums[0]-99;
        for (int j=0; j<nums.size()-1; j++) {
            // ! Since the array is sorted, we know it's not gonna make it.
            if (nums[j] > 0) break;

            // * Dedup.
            if (prev == nums[j]) continue;

            unordered_map<int, int> hashmap;
            int target = -nums[j];
            int used = -1;
            
            for (int i=j+1; i<nums.size(); i++) {
                int n = nums[i];
                if (hashmap.find(n) != hashmap.end()) {
                    // * Dedupe;
                    if (used>0 && hashmap[n]==used) continue;
                    // * Found a solution.
                    results.push_back(vector<int>{-target, nums[hashmap[n]], n});
                    used = hashmap[n];
                } else {
                    // * Store the residual.
                    int residual = target - n;
                    hashmap[residual] = i;
                }
            }
            prev = nums[j];
        }
        // vector<vector<int>> answer(results.begin(), results.end());
        return results;

    }
};