class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ## DFS with backtracking
        N, M = len(board), len(board[0])
        L = len(word)
        path = set()
        
        def dfs(i, j, index):
            if index == L:
                return True
            
            if i in range(N) and \
                j in range(M) and \
                index in range(L) and \
                (i,j) not in path and \
                board[i][j] == word[index]:

                path.add( (i,j) )
                        
                found = (dfs(i+1, j, index+1) or
                         dfs(i-1, j, index+1) or
                         dfs(i, j+1, index+1) or
                         dfs(i, j-1, index+1))
                path.remove( (i,j) )
                return found
            else:
                return False
        
        from collections import Counter
        board_counter = sum(map(Counter, board), start=Counter())
        word_counter = Counter(word)
        # * To prevent TLE, check if the board has enough chars for the word before going into the difficult part.
        for c, n in word_counter.items():
            if c not in board_counter or board_counter[c] < n:
                return False
        
        for r in range(N):
            for c in range(M):
                if dfs(r, c, 0):
                    return True

        return False
