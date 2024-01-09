class Solution:
    def shortestBridge(self, grid: List[List[int]]):
        """
        Shortest path with multiple srcs and dests
        [1,1,0,0,0],
        [1,1,0,0,1],
        [1,0,0,0,1],
        [0,0,0,0,1],
        [0,1,1,1,1]

        [0,1,0],
        [0,0,0],
        [0,0,1]

        [0,1],
        [1,0]

        • Scan and collect all the locations of one island
        • BFS on each src with inreasing radius
        • Stop once a source reaches the other part for the first time
        """
        N = len(grid)
        island1 = set()
        start = None
        for row in range(N):
            for col in range(N):
                if grid[row][col]:
                    start = (row, col)
                    break
            if start:
                break
        def in_grid(loc):
            if loc[0] < 0 or loc[0] >= N or loc[1] < 0 or loc[1] >= N:
                return False
            else:
                return True

        moves = [(-1,0), (1,0), (0,1), (0,-1)]
        def dfs(loc):
            if loc in island1 or not in_grid(loc):
                return
            if grid[loc[0]][loc[1]]:
                island1.add(loc)
            else:
                return
            
            for i, j in moves:
                dfs( (loc[0]+i, loc[1]+j) )
        #* Collect locations of the first island
        dfs(start)

        #* BFS from the first island.
        queue = list(island1)
        visited = island1.copy()
        steps = 0
        while steps < N:
            new_queue = []
            while queue:
                loc = queue.pop(0)
                for i, j in moves:
                    new_loc = (loc[0]+i, loc[1]+j)
                    if not in_grid(new_loc) or new_loc in visited:
                        continue
                    if grid[new_loc[0]][new_loc[1]]:
                        return steps
                    else:
                        visited.add(new_loc)
                        new_queue.append(new_loc)
            steps += 1
            queue = new_queue

        return 0
            
            
