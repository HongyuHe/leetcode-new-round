class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        Bottom up DP:
            * Columns: t, rows: s
            * Base case: extra column after t -- 0
            * Recursive relation: dp[i][j] = dp[i+1][j+1] + dp[i+1][j] if s[i] == t[j]
            * Final answer: dp[0][0]
        """
        ncols = len(t)
        nrows = len(s)
        dp = [[0 for _ in range(ncols+1)] for _ in range(nrows+1)]
        # Base case: If target 't' is empty (j == ncols), there is 1 way to match it.
        for i in range(nrows + 1):
            dp[i][ncols] = 1

        for i in range(nrows-1, -1, -1):
            for j in range(ncols-1, -1, -1):
                dp[i][j] = dp[i+1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
        return dp[0][0]
