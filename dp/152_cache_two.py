class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        cache = [[0,0] for _ in range(len(nums))]  # [min,max]
        cache[0] = [nums[0], 0] if nums[0] < 0 else [0, nums[0]]
        
        result = max(cache[0])
        for i in range(1, len(nums)):
            if nums[i] > 0:
                cache[i][0] = min( nums[i], nums[i]*cache[i-1][0] )    
                cache[i][1] = max( nums[i], nums[i]*cache[i-1][1] )  
            elif nums[i] < 0:
                cache[i][0] = min( nums[i], nums[i]*cache[i-1][1] )    
                cache[i][1] = max( nums[i], nums[i]*cache[i-1][0] )
            else:
                cache[i] = [0,0]
            
            result = max(result, cache[i][1])
        return result