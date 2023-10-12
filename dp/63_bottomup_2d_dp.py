class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]):
        if obstacleGrid[-1][-1]: 
            # * Handle edge case: the destination is an obstacle
            return 0
        # * Decision tree where each node has two branches: right and down
        # * One tile can be visited multiple times in a top-down approach
        rows = len(obstacleGrid) + 1
        cols = len(obstacleGrid[0]) + 1
        # * Base case initialized to 0's
        cache = [cols*[0] for _ in range(rows)]
        # * Destination
        cache[-2][-2] = 1

        for row in range(rows-2, -1, -1):
            for col in range(cols-2, -1, -1):
                if row == rows-2 and col == cols-2:
                    # * Don't overwrite the destination
                    continue
                if obstacleGrid[row][col] == 1:
                    # * Stand at an obstacle
                    continue

                # * total ways = down + right
                cache[row][col] = cache[row+1][col] + cache[row][col+1]

        return cache[0][0]


