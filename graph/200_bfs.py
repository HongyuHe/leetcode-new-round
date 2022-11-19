class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        ## Breadth first search (BFS)
        ## Do a BFS at each **unvisited** position
        ## Check their neighbors -> level by level
        ## [["1","1","1"],
        ##  ["0","1","0"],
        ##  ["1","1","1"]]
        N, M = len(grid), len(grid[0])
        visited = set()
        num_islands = 0
        
        def bfs(i, j):
            queue = deque([(i,j)])
            while queue:
                r, c = queue.popleft()
                if r in range(N) and \
                   c in range(M) and \
                   grid[r][c] == '1' and \
                   (r,c) not in visited:
                    
                    visited.add( (r,c) )
                    # * We have to add all 4 dirs.
                    queue.append((r+1, c))
                    queue.append((r-1, c))
                    queue.append((r, c+1))
                    queue.append((r, c-1))
            return
                    
                
        
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    num_islands += 1
        return num_islands
    