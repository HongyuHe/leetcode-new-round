class Solution:
    "20min"
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        2x2
        (0,0) -> (0,1)
        (0,1) -> (1,1)
        (1,0) -> (0,0)
        (1,1) -> (0,1)

        3x3
        (0,0) -> (0,2)
        (0,1) -> (1,2)
        (0,2) -> (2,2)

        * row[i] becomes col[n-i-1]
        * Save overwritten values

        Plan:
            * Move one row at a time.
            * Save overwritten values to a map.
            * Check the map before moving the row values.
        """
        #* (i,j) -> value
        cache = {}
        n = len(matrix[0])
        for i in range(n):
            # row = matrix[i]
            jj = n - i - 1
            for j in range(n):
                if (i,j) in cache:
                    value = cache[(i,j)]
                    #* Save memory, cache max one row.
                    #? Doesn't seem to have much effect on memory usage?
                    del cache[(i,j)]
                else: 
                    value = matrix[i][j]
                ii = j
                #* Store the current value before overwriting it.
                cache[(ii,jj)] = matrix[ii][jj]
                matrix[ii][jj] = value

