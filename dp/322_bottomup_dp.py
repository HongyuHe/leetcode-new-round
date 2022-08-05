class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1: return 0
        
        ledger = [0] * (amount+1)
        
        for target in range(1, amount+1):
            results = []
            for coin in coins:
                residual = target - coin
                
                if residual == 0:
                    results.append(1)
                    break
                elif residual > 0 and ledger[residual] > 0:
                    results.append(
                        ledger[residual] + 1  #* Build upon previous results.
                    )
                else: 
                    continue
                    
            ledger[target] = min(results) if results else -1
            # print(ledger)
        
        return ledger[-1]
