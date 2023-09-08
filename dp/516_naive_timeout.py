class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # * For each character, we have two choices---taking it or not taking it.
        # * -> Brute-focing (backtracking): try every single combination and 
        # * prun the decision tree along the way.
        # * Worst case: O(n * 2^n) -> should be much better in practice :)
        total_len = len(s)

        def is_palindrome(substr):
            mid = len(substr) // 2
            for i in range(mid):
                if substr[i] != substr[-i-1]:
                    return False
            return True
        
        def dfs(pos, substr, longest_len):
            if pos == total_len:
                return longest_len
            
            if is_palindrome(substr):
                longest_len = max(longest_len, len(substr))

            for i in range(pos+1, total_len):
                # Choice 1: taking the char.
                take_len = dfs(i, substr+s[i], longest_len)
                # Choice 2: not taking the char.
                notake_len = dfs(i, substr, longest_len)
                longest_len = max(take_len, notake_len)
                
            return longest_len

        return dfs(-1, '', 0)


