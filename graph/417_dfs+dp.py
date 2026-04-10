class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """ 40min, failed.
        Question: Ordering of the output cells?
        Plan:
        * DP problem, 2 passes: can get to Pacific? + can get to Atlantic?
        * Return cells that can get to both.
        """
        nrows = len(heights)
        ncols = len(heights[0])
        
        pacific_cache = [[None for _ in range(ncols)] for _ in range(nrows)]
        atlantic_cache = [[None for _ in range(ncols)] for _ in range(nrows)]
        
        #* Set the base cases
        for row in range(nrows):
            pacific_cache[row][0] = True
            atlantic_cache[row][-1] = True
        for col in range(ncols):
            pacific_cache[0][col] = True
            atlantic_cache[-1][col] = True
        
        # 1. ADD `visited` TO THE PARAMETERS
        def is_reachable(row, col, cache, visited):
            # If we already know the definitive answer, return it
            if cache[row][col] is not None:
                return cache[row][col]
                
            # 2. CYCLE PREVENTION: If we are already looking at this cell in the current path, 
            # assume False for this specific route to prevent an infinite loop.
            if (row, col) in visited:
                return False
                
            # Mark the current cell as visiting for this path
            visited.add((row, col))
            height = heights[row][col]

            # NOTE: Changed > 0 to >= 0 so the recursion can actually reach the ocean base cases!
            if row-1 >= 0 and heights[row-1][col] <= height and is_reachable(row-1, col, cache, visited):
                cache[row][col] = True
                return True
            if col-1 >= 0 and heights[row][col-1] <= height and is_reachable(row, col-1, cache, visited):
                cache[row][col] = True
                return True
            if row+1 < nrows and heights[row+1][col] <= height and is_reachable(row+1, col, cache, visited):
                cache[row][col] = True
                return True
            if col+1 < ncols and heights[row][col+1] <= height and is_reachable(row, col+1, cache, visited):
                cache[row][col] = True
                return True

            #! Important: Remove from visited before returning (Backtracking)
            visited.remove((row, col))
            
            # Note on caching False: In Top-Down DP with cycles, caching False here is technically 
            # unsafe because a cell might have returned False just because it hit the `visited` set 
            # from this specific path, but could still be true via another path. 
            # However, for the sake of your original logic, we leave your structure intact:
            # cache[row][col] = False 
            return False
            

        #* Pacific pass
        for row in range(1, nrows):
            for col in range(1, ncols):
                # 3. PASS A NEW SET ON EVERY STARTING CALL
                is_reachable(row, col, pacific_cache, set())
                
        flowables = []
        
        #* Atlantic pass
        for row in range(nrows-1, -1, -1):
            for col in range(ncols-1, -1, -1):
                # 3. PASS A NEW SET ON EVERY STARTING CALL
                if is_reachable(row, col, atlantic_cache, set()) and pacific_cache[row][col]:
                    flowables.insert(0, [row, col])
                    
        return flowables