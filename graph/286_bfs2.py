class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """ BFS with a single queue
        """
        nrows = len(grid)
        ncols = len(grid[0])
        INF = 2147483647

        chest_pos = []
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == 0:
                    chest_pos.append((row, col)) 
        
        def get_next_steps(row, col, queue):
            if row-1 >= 0:
                queue.append((row-1, col))
            if col-1 >= 0:
                queue.append((row, col-1))
            if row+1 < nrows:
                queue.append((row+1, col))
            if col+1 < ncols:
                queue.append((row, col+1))
            return

        from collections import deque 
        dist = 0
        queue = deque(chest_pos)
        while queue:
            level_size = len(queue)
            #! Only pop the next level to keep track of the distance/radius
            for _ in range(level_size):
                row, col = queue.popleft()
                val = grid[row][col]
                keep_going = val == 0
                if val > dist:
                    grid[row][col] = dist
                    #* Need to keep updating furter
                    keep_going = True
                if keep_going:
                    get_next_steps(row, col, queue)
            dist += 1
