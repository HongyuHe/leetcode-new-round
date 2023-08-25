class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # * Break down the problem into subproblems by doing bottom-up on both sequences.
        # * -> 2D DP
        # * Example: "abcde" "bcbce"
        #     a b c d e
        #     0 0 0 0 0
        # b 0 0 1 1 
        # c 0     2 
        # b 0       2 0
        # c 0       2 2 
        # e 0       2 3

        # * With base case.
        cols = len(text1) + 1
        rows = len(text2) + 1
        dp_table = [[0] * cols for _ in range(rows)] 

        # ? Do we really need to traverse the whole matrix?
        for i in range(1, rows):
            for j in range(1, cols):
                if text2[i-1] == text1[j-1]:
                    dp_table[i][j] = dp_table[i-1][j-1] + 1
                else:
                    # * Take the best of both subproblems.
                    dp_table[i][j] = max(dp_table[i][j-1], dp_table[i-1][j])
        return dp_table[-1][-1]
