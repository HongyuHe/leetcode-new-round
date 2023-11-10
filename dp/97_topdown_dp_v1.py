class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Two pointers
            s1=ab a s2=a b b s3=ab a b a b
        """
        if len(s1) + len(s2) != len(s3):
            return False


        end1 = len(s1)
        end2 = len(s2)
        end3 = len(s3)
        cache = [[-1] * (end2+1) for _ in range(end1+1)]

        def dfs(p1, p2, p3):
            if p3 == end3:
                #* Reached the end.
                if p1 == end1 and p2 == end2:
                    #* Used up chars in both strings.
                    cache[p1][p2] = 1
                    return True
                else:
                    cache[p1][p2] = 0
                    return False

            if cache[p1][p2] >= 0:
                return cache[p1][p2]

            char = s3[p3]
            if p1 < end1 and p2 < end2 and char == s1[p1] == s2[p2]:
                matched = dfs(p1+1, p2, p3+1)
                if matched:
                    cache[p1][p2] = 1
                else:
                    cache[p1][p2] = dfs(p1, p2+1, p3+1)
            elif p1 < end1 and char == s1[p1]:
                cache[p1][p2] = dfs(p1+1, p2, p3+1)
            elif p2 < end2 and char == s2[p2]:
                cache[p1][p2] = dfs(p1, p2+1, p3+1)
            else:
                #* No match at p3
                cache[p1][p2] = 0

            return True if cache[p1][p2] else False
        
        return dfs(0, 0, 0)
        