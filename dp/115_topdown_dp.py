class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        Reduction:
            * Search problem (dfs), each char of `s` has two choice: use or skip -> 2^1000
            * Naive: enumerate all possible choices on `s` with two indices walking s and t respectively.
                * Only move the pointer if the pointed chars match
            * Optimization: find repeated subprobs and use a memoization
        """
        cache = {}
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            count = 0
            if s[i] == t[j]:
                count += dfs(i+1, j+1)
            count += dfs(i+1, j)
            cache[(i, j)] = count
            return count
        return dfs(0, 0)
    