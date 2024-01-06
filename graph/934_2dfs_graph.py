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

        tried = set()
        def find_island2(loc, steps):
            if steps < 0 or not in_grid(loc) or (loc, steps) in tried:
                return False
            if grid[loc[0]][loc[1]] and loc not in island1:
                return True
            else:
                for i,j in moves:
                    new_loc = (loc[0]+i, loc[1]+j)
                    if find_island2(new_loc, steps-1):
                        return True
                    else:
                        tried.add((new_loc, steps-1))

        radius = 1
        while radius <= N:
            for loc in island1:
                for i, j in moves:
                    new_loc = (loc[0]+i, loc[1]+j)
                    if (new_loc, radius) in tried:
                        continue
                    if find_island2(new_loc, radius):
                        return radius
                    else:
                        tried.add((new_loc, radius))
            radius += 1

        return 0
            
            
