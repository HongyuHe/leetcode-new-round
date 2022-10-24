class Solution:
    def longestPalindrome(self, s: str) -> str:
        cache = [[0]*len(s) for _ in range(len(s))]
        longest_len = 1
        longest_str = s[0]
        
        for i in range(len(s)): cache[i][i] = 1
        
        for d in range(1, len(s)):
            for i in range(len(s)-d):
                if s[i] == s[i+d]:
                    if d == 1 or cache[i+1][i+d-1]:
                        cache[i][i+d] = 1
                        if d+1 > longest_len:
                            longest_str = s[i: i+d+1]    
                
        return longest_str
