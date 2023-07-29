class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # * Example: coins = [1,2,5], amount = 6 -> (1, 5) -> 2
        # * cache = [0, 1, 1, 2, 2, 1, 2]

        if not amount: 
            return 0

        MAX = 10**5
        # * Caches the fewest number of coins to achieve amount i.
        cache = [-1] * (amount+1)
        cache[0] = 0

        for target in range(1, amount+1):
            fewest = MAX
            for coin in coins:
                residual = target - coin
                if residual >= 0 and cache[residual] >= 0:
                    fewest = min(fewest, cache[residual])
            if fewest != MAX:
                cache[target] = fewest + 1

        return cache[-1]
