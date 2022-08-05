class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 1: return 0
        
        cache = {}
        def dfs(num, total):
            if total in cache:
                return cache[total]
            
            _results = []
            for coin in coins:
                if total + coin < amount:
                    _results.append(
                        dfs(num+1, total+coin)  #! This is wrong -- I shouldn't cache how the leaves are reached.
                    )
                elif total + coin > amount: 
                    _results.append(
                        float('inf')  # Unreachable.
                    )  
                elif total + coin == amount:
                    return num+1  # Return immediately since it's the local best.
            
            cache[total] = min(_results)
            return cache[total]
        
        answer = dfs(0, 0)
        return answer if answer != float('inf') else -1
    
    
        