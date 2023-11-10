class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str):
        """ 
        cache[p1][p2]: Can we interleave s1[p1: ] and s2[p2: ] to form s3[(p1+p2): ]
        • Base case: cache[len(s1)][len(s2)]: Reached the end of s3 (p1+p2=p3) -> True
        • Target: aadbbcbcac
                  a a b c c _
                d 
                b
                b
                c
                a         1 0
                _         1 1
        """
        len1 = len(s1)
        len2 = len(s2)

        if len1 + len2 != len(s3):
            return 0
        
        #* Initialize all to false.
        cache = [[0] * (len2+1) for _ in range(len1+1)]

        #* Bottom up
        for p1 in range(len1, -1, -1):
            for p2 in range(len2, -1, -1):
                if p1 == len1 and p2 == len2:
                    #* Set the base case to true where both pointers reach the end.
                    cache[p1][p2] = 1
                    continue
                
                char = s3[p1+p2]
                if p1 < len1 and s1[p1] == char and cache[p1+1][p2]:
                    cache[p1][p2] = 1
                elif p2 < len2 and s2[p2] == char and cache[p1][p2+1]:
                    cache[p1][p2] = 1
                # else:
                    #* All initialized to 0's already.
                    # cache[p1][p2+1] = 0
            
        return cache[0][0]

        