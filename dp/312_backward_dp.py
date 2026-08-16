class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        Idea:
            * Create independent subproblems by starting from last-burst ballons
            * State: (left, right) pair demarcating the subarrays -- O(N^2)
            * The left and right indices are sure to neighbor with the last-burst ballons
            * Pad the nums with 1's 
        Example:
            [1,3,1,5,8,1]
        """
        nums = [1] + nums + [1]
        cache = {}

        def dfs(left, right) -> int:
            if left == right:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]
            
            maxcoins = 0
            for i in range(left+1, right):
                coins = nums[left] * nums[i] * nums[right]
                coins += dfs(left, i)
                coins += dfs(i, right)

                maxcoins = max(coins, maxcoins)
            
            cache[(left, right)] = maxcoins
            return maxcoins
        return dfs(0, len(nums)-1)