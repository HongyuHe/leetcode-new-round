class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ## Start from the finish line
        ## Only move to left and up
        ## Every position is the sum of its right and down
        
        grid = [[0]*(n+1) for _ in range(m+1)]
        
        for row in reversed(range(m)):
            for col in reversed(range(n)):
                # print(row, col)
                if row == m-1 and col == n-1:
                    grid[row][col] = 1 # * Finish line.
                else:
                    grid[row][col] = grid[row+1][col] + grid[row][col+1]
        return grid[0][0]
        