class Solution:
    def numDecodings(self, s: str) -> int:
        ## Input: s = "226"
        ##   - 2 2   6   1   5
        ##   1 1 1+1 2+1 3+0 3+3 => 6
        
        if s[0] == '0': return 0
        
        cache = [0] * (len(s)+1)
        cache[0] = 1
        for i, char in enumerate(s):
            i += 1
            # * Stand-alone.
            count = 0
            if char != '0':
                count += cache[i-1]
            # * Look one digit back.
            if i > 1 and s[i-2] != '0' and int(s[i-2: i]) <= 26:
                count += cache[i-2]
            cache[i] = count
        
        return cache[-1]
        