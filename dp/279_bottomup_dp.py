class Solution:
    def numSquares(self, n: int) -> int:
        # * Example: n=12
        # [0, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        # [0, 1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        # [0, 1, 2, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        # [0, 1, 2, 3, 1, -1, -1, -1, -1, -1, -1, -1, -1]
        # [0, 1, 2, 3, 1, 2, -1, -1, -1, -1, -1, -1, -1]
        # [0, 1, 2, 3, 1, 2, 3, -1, -1, -1, -1, -1, -1]
        # [0, 1, 2, 3, 1, 2, 3, 4, -1, -1, -1, -1, -1]
        # [0, 1, 2, 3, 1, 2, 3, 4, 2, -1, -1, -1, -1]
        # [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, -1, -1, -1]
        # [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, -1, -1]
        # [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, -1]
        # [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 3]
        cache = [-1] * (n+1)
        # * Base case.
        cache[0] = 0 

        MAX = 10**4
        for target in range(1, n+1):
            min_count = MAX
            for i in range(1, int(target**0.5)+1):
                s = i**2
                min_count = min(min_count, cache[target-s])
            # * Take into account the current perfect square s.
            cache[target] = min_count + 1
        
        return cache[-1]
        