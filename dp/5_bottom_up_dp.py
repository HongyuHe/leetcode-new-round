class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Cache[i][j]: s[i] - s[j] T if palindrome else F
        cache = [[0]*len(s) for _ in range(len(s))]
        longest_len = 1
        longest_str = s[0]
        
        # If I put this initialization inside the main loop (i.e., 15-16), this solution will timeout.
        for i in range(len(s)):
            cache[i][i] = 1
        
        for d in range(1, len(s)):
            for i in range(len(s)-d):
                # if i+d >= len(s): continue
                # if d == 0:
                #     cache[i][i+d] = 1
                if d == 1:
                    cache[i][i+d] = 1 if s[i] == s[i+d] else 0
                else:
                    # Check the middle
                    if cache[i+1][i+d-1]:
                        # Compare the start and the end
                        cache[i][i+d] = 1 if s[i] == s[i+d] else 0
                        
                if cache[i][i+d] and d+1 > longest_len:
                    longest_str = s[i: i+d+1]
                
                # print(cache)
                
        return longest_str
