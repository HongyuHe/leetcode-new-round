class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # * (idx, total) -> number of ways to achieve `target` given `nums[:idx]`.
        cache = {}
        def dfs(idx, total):
            if idx == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            
            key = (idx, total)
            if key in cache:
                return cache[key]
            
            ways = dfs(idx+1, total+nums[idx]) + dfs(idx+1, total-nums[idx])
            # * Cache the results.
            cache[key] = ways
            return ways
        
        return dfs(0, 0)
