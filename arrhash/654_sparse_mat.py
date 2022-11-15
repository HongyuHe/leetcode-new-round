from typing import (
    List,
)

class Solution:
    """
    @param a: a sparse matrix
    @param b: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        result = [[0]*len(b[0]) for _ in range(len(a))]
        
        for row in range(len(a)):
            for col in range(len(b[0])):
                a_row = a[row]
                b_col = [b[i][col] for i in range(len(b))]
                result[row][col] = sum([ai * bi for (ai, bi) in zip(a_row, b_col)])
        # print(result)
        return result
        