class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1] * len(nums)
        
        for i in range(1, len(nums)):
            max_len = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    max_len = max(max_len, cache[j]+1) 
            cache[i] = max_len
        return max(cache)
                    