class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # * Example: 
        # * coin/target     0    1   2   3   4   5
        # *         0       1    0   0   0   0   0
        # *         1       1  1+0 1+0 1+0 1+0 1+0
        # *         2       1    1 1+1 1+1 1+2 1+2
        # *         5       1    1   1   1   1 3+1


        # * cache[coin_idx][target]: 
        # *     number of ways to achieve `target` using only `coins[:coin_idx]`
        rows = len(coins) + 1
        cols = amount + 1
        cache = [cols*[0] for _ in range(rows)]
        # * Base case
        for i in range(cols):
            # * Having no coins
            cache[0][i] = 0
        for i in range(rows):
            # * One way of achieving amount=0
            cache[i][0] = 1
        
        for i in range(1, rows):
            coin = coins[i-1]
            for target in range(1, amount+1):
                # * Do NOT use this `coin` -> Go one row above (discarding this coin)
                cache[i][target] = cache[i-1][target]
                # * Use this `coin`
                residual = target - coin
                if residual >= 0:
                    cache[i][target] += cache[i][residual]

        return cache[-1][-1]
