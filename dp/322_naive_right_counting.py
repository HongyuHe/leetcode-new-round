class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(residual):
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
            return result + 1 if result != float('inf') else float('inf')
        
        count = dfs(amount)
        return count if count != float('inf') else -1
            
            