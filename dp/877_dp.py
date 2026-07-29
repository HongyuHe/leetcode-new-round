class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """ 29min one attempt
        Reduction: Can we find ONE way for the first mover to win?
            * Search problem 
            * Exhaustive 
        Naive: 
            * Try every combo where Alice starts first
            * Check if there's combo whose sum > 1/2 total
        Plan:
            * Use caching (DP memorization)
        """
        target = sum(piles) / 2
        max_decisions = len(piles) / 2
        cache = {}
        def dfs(idx: int, total: int):
            if (idx, total) in cache:
                return cache[(idx, total)]
            if total > target:
                cache[(idx, total)] = True
                return True
            if idx > max_decisions:
                cache[(idx, total)] = False
                return False
            
            if dfs(idx+1, total + piles[idx]) or dfs(idx+1, total + piles[-idx]):
                cache[(idx, total)] = True
                return True
            else:
                cache[(idx, total)] = False
                return False
        
        return dfs(0, 0)