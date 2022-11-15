class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ##     a c e
        ##   0 0 0 0
        ## a 0 1 1 1
        ## b 0 1 1 1
        ## c 0 1 2 2
        ## d 
        ## e
        cache = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]     

        for row in range(1, len(text1)+1):
            for col in range(1, len(text2)+1):
                i = row-1
                j = col-1
                if text1[i] == text2[j]:
                    cache[row][col] = cache[row-1][col-1]+1
                else:
                    cache[row][col] = max(cache[row-1][col], cache[row][col-1])
                
                # for n in cache: print(*n, sep=' '); print()
        return cache[len(text1)][len(text2)]
                
                    