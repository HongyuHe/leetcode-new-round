class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """ 20min
        https://neetcode.io/problems/islands-and-treasure/question
        Plan:
            * Find all treasure troves
            * Simultaneously expand from the chests using BFS.
            * Only update the cell if its value is greater than the distance we gonna update it to.
        """
        nrows = len(grid)
        ncols = len(grid[0])
        INF = 2147483647

        chest_pos = []
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == 0:
                    chest_pos.append((row, col)) 
        
        def get_next_steps(row, col):
            steps = []
            if row-1 >= 0:
                steps.append((row-1, col))
            if col-1 >= 0:
                steps.append((row, col-1))
            if row+1 < nrows:
                steps.append((row+1, col))
            if col+1 < ncols:
                steps.append((row, col+1))
            return steps

        from collections import deque 
        dist = 0
        queue = deque(chest_pos)
        nxt_level = []
        while queue:
            row, col = queue.popleft()
            val = grid[row][col]
            keep_going = val == 0
            if val > dist:
                grid[row][col] = dist
                #* Need to keep updating furter
                keep_going = True
            if keep_going:
                nxt_steps = get_next_steps(row, col)
                nxt_level += nxt_steps
            
            if not queue:
                #* Move on to the next BFS level
                dist += 1
                queue = deque(nxt_level)
                nxt_level = []
