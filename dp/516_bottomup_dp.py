class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # * Use the solution to the LSC with the 2nd sequence being the reverse of `s`.
        rs = s[::-1]
        n = len(s) + 1 # * Need base cases at the start.
        dp_table = [[0] * n for _ in range(n)]

        for i in range(1, n):
            for j in range(1, n):
                # * Go back one place to index the strings.
                if s[i-1] == rs[j-1]:
                    # * Go diagonally.
                    dp_table[i][j] = dp_table[i-1][j-1] + 1
                else:
                    # * Choose one of the two chars to continue.
                    dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])
        
        return dp_table[-1][-1]