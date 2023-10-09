class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # * Worst case: N^N for N coins
        # * Example: amount=3, coins=[1,2,5]
        # * cache: [1,0,0,0] 
        # *     target=1 => [1,1,0,0]
        # *     target=2 => [1,1,1+1=2,0]
        # *     target=3 => [1,1,2,2+1]

        if amount == 0: return 1

        cache = [0] * (amount+1)
        # * Base case
        cache[0] = 1

        for target in range(1, amount+1):
            for coin in coins:
                residual = target - coin
                if residual >= 0:
                    cache[target] += cache[residual]

        return cache[-1]