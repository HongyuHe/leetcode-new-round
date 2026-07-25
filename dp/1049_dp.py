class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        Reduction: Select two groups of numbers whose sums are as similar as possible
        Plan:
            * DFS for the search, goal: find the pile having the sum closest to helf of the total.
            * Use DP (memoization): There could be multiple paths reaching the same decision point (stone index and the current weight).
        """
        total = sum(stones)
        target = total // 2
        cache = {}

        def dfs(i, partial_sum):
            if (i, partial_sum) in cache:
                return cache[(i, partial_sum)]
            if partial_sum >= target or i >= len(stones):
                diff = abs(total - 2 * partial_sum)
                return diff

            diff_in = dfs(i+1, partial_sum + stones[i])
            diff_ex = dfs(i+1, partial_sum)
            cache[(i, partial_sum)] = min(diff_in, diff_ex)
            return cache[(i, partial_sum)]
        
        return dfs(0, 0)