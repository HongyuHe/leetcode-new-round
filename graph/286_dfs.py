class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """ Attempt 1: 25min failed. Attempt 2: 10min-fix passed.
        https://neetcode.io/problems/islands-and-treasure/question
        Plan:
            * Start from the treasure troves
            * "Flood" from the troves using dfs to update the distances
                * If it's land, overwrite it.
                * If it's a positive integer, update it iff the distance is smaller.
        """
        INF = 2147483647
        nrows = len(grid)
        ncols = len(grid[0])
        def dfs(row, col, dist, path):
            if (row < 0 or row == nrows or col < 0 or col == ncols 
                or grid[row][col] == -1
                or (row, col) in path):
                return
            
            val = grid[row][col]
            if val > dist:
                grid[row][col] = dist
                # if val == INF:
                #     #* Just overwrite it.
                #     grid[row][col] = dist
                # else:
                #     if val > dist:
                #         grid[row][col] = dist
            if val == 0 or val > dist:
                path.add( (row, col) )
                #* Go 4 directions.
                dist += 1
                dfs(row+1, col, dist, path)
                dfs(row-1, col, dist, path)
                dfs(row, col+1, dist, path)
                dfs(row, col-1, dist, path)
                path.remove( (row, col) )
        
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == 0:
                    dfs(row, col, 0, set())
        