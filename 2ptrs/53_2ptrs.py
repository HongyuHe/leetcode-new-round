class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ## Brute force: try all combinations of starting and ending positions
        ## Two pointers: l -> start; r -> end. => Discard all negative prefixes.
        ## [-2,1,-3,4,-1,-1,2,1,-5,4]
        ## [-2,1]
        ## [-1,1,2,1]
        ## [5,4,-1,7,8]
        
        max_sum = max(nums)
        if len(nums) == 1: return max_sum
        
        l, r = 0, 0
        cur_sum = 0
        while r < len(nums):
            cur_sum += nums[r]
            if cur_sum < 0:
                cur_sum = 0
                # * Only discard the prefix arr if the sum is negative -> greedy.
                l = r+1
            else:
                max_sum = max(max_sum, cur_sum)
            r += 1
        #> r==len(nums)
        return max_sum
        