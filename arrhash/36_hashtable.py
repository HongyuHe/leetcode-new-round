class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # * Validate the rows.
        for row in board:
            table = {}            
            for e in row:
                count = table.get(e, 0)
                if count != 0 and e != '.':
                    return False
                else:
                    table[e] = count+1
        # * Valide the cols.
        for col in range(9):
            table = {}
            for row in range(9):
                e = board[row][col]
                count = table.get(e, 0)
                if count != 0 and e != '.':
                    return False
                else:
                    table[e] = count+1
        # * Valide the submatrices.
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                table = {}            
                for r in range(3):
                    i = row + r
                    for c in range(3):
                        j = col + c
                        e = board[i][j]
                        count = table.get(e, 0)
                        if count != 0 and e != '.':
                            return False
                        else:
                            table[e] = count+1
        return True
                        
                
                    
                
