class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """ 20m, one attempt
        Plan:
            * Scan the grid row by row
            * If encounter a land cell, do a DFS to get the area
            * Keep `visited` and `max_area`
        
        Complexity
            * Time: O(m x n)
            * Space: O(m x n)
        """
        area_max = 0
        visited = set()
        nrows = len(grid)
        ncols = len(grid[0])

        def dfs(row, col, area):
            if row < 0 or row >= nrows or col < 0 or col >= ncols:
                return area
            
            if (row, col) in visited:
                return area

            cell = grid[row][col]
            if not cell:
                return area
            
            visited.add((row, col))
            area += 1

            area += dfs(row-1, col, 0)
            area += dfs(row+1, col, 0)
            area += dfs(row, col+1, 0)
            area += dfs(row, col-1, 0)
            return area
            

        for row in range(nrows):
            for col in range(ncols):
                cell = grid[row][col]
                if cell and (row, col) not in visited:
                    #* Found a new piece of land.
                    area = dfs(row, col, 0)
                    area_max = max(area_max, area)
        return area_max