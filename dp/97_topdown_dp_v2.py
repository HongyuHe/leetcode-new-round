class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Two pointers
            s1=ab a s2=a b b s3=ab a b a b
        """
        if len(s1) + len(s2) != len(s3):
            return 0
        
        #* Actually only need to cache unsuccessful cases.
        #* (return immedeiately upon a True)
        cache = [[-1] * (len(s2)+1) for _ in range(len(s1)+1)]

        def dfs(p1, p2):
            #* Reached the end.
            if p1 == len(s1) and p2 == len(s2):
                #* Used up chars in both strings.
                return 1

            if cache[p1][p2] >= 0:
                return cache[p1][p2]

            #* p3 = p1 + p2
            char = s3[p1+p2]
            if p1 < len(s1) and char == s1[p1] and dfs(p1+1, p2):
                return 1
            elif p2 < len(s2) and char == s2[p2] and dfs(p1, p2+1):
                return 1
            else:
                #* No match at either s1 or s2
                cache[p1][p2] = 0
                return 0
        
        return dfs(0, 0)
        