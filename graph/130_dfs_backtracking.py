class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """ 20min
        Plan: 
            * Go around edge and mark those non-surrounded 0-cells -- dfs
            * Traverse the inner board and replace all non-marked 0-cells
        Complexity:
            * Time: O(MxN)
            * Space: O(MxN)
        """
        nrows = len(board)
        ncols = len(board[0])
        preserved_cells = set()
        visited = set()

        def dfs(row, col, path):
            if row < 0 or row >= nrows or col < 0 or col >= ncols:
                return
            if (row, col) in path or (row, col) in visited:
                return
            
            #* Global visited set!
            visited.add( (row, col) )

            if board[row][col] == 'X':
                return

            path.add( (row, col) )
            preserved_cells.add( (row, col) )
            dfs(row+1, col, path)
            dfs(row-1, col, path)
            dfs(row, col+1, path)
            dfs(row, col-1, path)
            #* Backtracking
            path.remove( (row,col) )
        
        #* Go around the edge
        for row in range(nrows):
            dfs(row, 0, set())
            dfs(row, ncols-1, set())
        for col in range(nrows):
            dfs(0, col, set())
            dfs(nrows-1, col, set())
        
        #* Traverse the inner cells
        for row in range(1, nrows-1):
            for col in range(1, ncols-1):
                if (row, col) not in preserved_cells:
                    board[row][col] = 'X'
        