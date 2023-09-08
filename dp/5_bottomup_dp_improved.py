class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # * cache[start][start+dist]==True if s[start: start+dist] is palindrome.
        cache = [[False]*n for _ in range(n)]
        longest_len = 1
        longest_str = s[0]
        
        for i in range(n): 
            # * Base case: single letters are always palindromes.
            cache[i][i] = True
        
        for d in range(1, n):
            # * Gradually increase the distance `d` from pos `start`.
            for start in range(n-d):
                # * Compare two characters of distance `d`.
                if s[start] == s[start+d]:
                    # * If substring `s[(start)+1, (start+d)-1]` is a palindrome 
                    # * I.e., we shrink one place on both sides (subproblem).
                    # * Or special case: d==1 -> two-letter string, e.g., "bb"
                    if cache[start+1][start+d-1] or d == 1:
                        # * Then `s[start: start+d]` is also a palindrome. 
                        cache[start][start+d] = True
                        # * Chekc a longer one has been found.
                        if d+1 > longest_len:
                            longest_str = s[start: start+d+1]   
                
        return longest_str
