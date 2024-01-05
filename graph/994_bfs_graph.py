class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        * Collect all the starting coords AND the # of fresh oranges
        * BFS using a queue for traversal
        * Stop if no fresh organges OR empty queue
        """
        rows = len(grid)
        cols = len(grid[0])

        queue = []
        num_fresh = 0
        #* O(m*n)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    num_fresh += 1

        if num_fresh == 0:
            return 0

        #* O(m*n)
        minutes = 0
        while queue:
            minutes += 1
            nxt_level = []
            while queue:
                i, j = queue.pop(0)
                    
                if (i+1) < rows and grid[i+1][j] == 1:
                    num_fresh -= 1
                    grid[i+1][j] = 2
                    nxt_level.append((i+1, j))
                if (j+1) < cols and grid[i][j+1] == 1:
                    num_fresh -= 1
                    grid[i][j+1] = 2
                    nxt_level.append((i, j+1))
                if (i-1) >= 0 and grid[i-1][j] == 1:
                    num_fresh -= 1
                    grid[i-1][j] = 2
                    nxt_level.append((i-1, j))
                if (j-1) >= 0 and grid[i][j-1] == 1:
                    num_fresh -= 1
                    grid[i][j-1] = 2
                    nxt_level.append((i, j-1))
            
                if num_fresh == 0:
                    break
            if num_fresh == 0:
                break

            queue = nxt_level

        return minutes if num_fresh==0 else -1