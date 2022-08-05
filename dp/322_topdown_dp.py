class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}  # [residual] = count
        
        def dfs(residual):
            if residual in cache:
                return cache[residual]
            
            if residual == 0:
                return 0
            elif residual < 0:
                return float('inf')
            
            results = []
            # Continue plunging.
            for coin in coins:
                results.append(
                    dfs(residual - coin)
                )
            
            result = min(results)
            result = result + 1 if result != float('inf') else float('inf')
            cache[residual] = result
            return result
        
        count = dfs(amount)
        return count if count != float('inf') else -1
            
            