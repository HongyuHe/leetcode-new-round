class Solution {
public:
    int getMaxLen(vector<int>& nums) {
        int longest = 0;
        for (int start = 0; start < nums.size(); start++) {
            if (longest >= nums.size() - start) { break; }
            if (nums.at(start) == 0) { continue; }
            
            // double prod = 1;
            int neg_count = 0;
            for (int i = start; i < nums.size(); i++) {
                if (nums.at(i) < 0) {
                    neg_count++;
                } else if (nums.at(i) == 0) {
                    break;
                }
                if (neg_count % 2 == 0) {
                    longest = max(i - start + 1, longest); 
                }
                //! Multiplication is too expensive and will cause timeout!!!
                // prod *= nums.at(i);
                // if (prod > 0) {
                //     longest = std::max(i - start + 1, longest); 
                // } else if (prod == 0) {
                //     break;
                // }
            }
        }
        return longest;
    }
};