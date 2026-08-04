class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
        Attemp 1: OOT(18min), Attemp 2: 20min -- fixed indexing, prefix sum
        Notes:
            * Pushing up M helps the opponent as well
        """
        cache = {}

        def dfs(idx: int, M: int, myturn: bool):
            if (idx, M, myturn) in cache:
                return cache[(idx, M, myturn)]
            if idx == len(piles):
                return 0
            
            maxcount = 0
            prefix_sum = 0
            if myturn:
                for m in range(1, 2*M+1):
                    if idx+m-1 < len(piles):
                        prefix_sum += piles[idx+m-1]
                        maxcount = max(prefix_sum + dfs(idx+m, max(m, M), False), maxcount)
            else:
                maxcount = float("inf")
                for m in range(1, 2*M+1):
                    if idx+m-1 < len(piles):
                        maxcount = min(dfs(idx+m, max(m, M), True), maxcount)
            cache[(idx, M, myturn)] = maxcount
            return maxcount
        return dfs(0, 1, True)