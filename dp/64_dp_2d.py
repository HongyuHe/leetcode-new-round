class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Analysis:
            * Only go right or bottom
            * The grid is a rectangle
        Naive approach:
            * DFS enumerating all possible paths
            * Repeated subproblems 
                * "5" can be reached in multiple paths (through "11" and "13")
                * Doesn't matter from which path it was reached -> independent subproblems
        Plan: Bottom up DP
            * Build cache starting from the bottom right (destination)
            * Each cell is the smallest path sum to the dest
            * A new cell: its-val + min(right, bottom)
        """
        nrows = len(grid)
        ncols = len(grid[0])
        sums = [[0 for _ in range(ncols+1)] for _ in range(nrows+1)]

        #* Initialize the base case:
        for row in range(nrows-1):
            sums[row][-1] = float('inf')
        for col in range(ncols-1):
            sums[-1][col] = float('inf')
        

        for i in range(nrows-1, -1, -1):
            for j in range(ncols-1, -1, -1):
                sums[i][j] = grid[i][j] + min(sums[i][j+1], sums[i+1][j])

        return sums[0][0]