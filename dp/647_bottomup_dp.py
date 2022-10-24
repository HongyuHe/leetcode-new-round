class Solution:
    def countSubstrings(self, s: str) -> int:
        cache = [[0]*len(s) for _ in range(len(s))]
        count = len(s)
        
        ## Base case
        for i in range(len(s)): 
            cache[i][i] = 1
        
        for dist in range(1, len(s)):                
            for start in range(len(s)-dist):
                end = start + dist
                if s[start] == s[end]:
                    if dist == 1 or cache[start+1][end-1]:
                        cache[start][end] = 1
                        count += 1
        return count