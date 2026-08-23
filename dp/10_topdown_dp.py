class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        More examples:
            * s = "a" p = "a*a"
            * s = "aaab" p = "c*a*b"
        Plan:
            * Check for * in the next positon of p
            * At each position of s, we decide whether to use the star or not if given the choice
            * Top down momoization DP
        """
        
        cache = {}
        def dfs(i: int, j: int) -> bool:
            if (i, j) in cache:
                return cache[(i, j)]
            if i == len(s) and j >= len(p):
                return True
            if (i == len(s) and j == len(p)-1 and p[j] == '*'):
                return True
            if i < len(s) and j >= len(p):
                return False
            
            matched = False
            # Check if the pattern is a star
            if p[j] == '*':
                if i == len(s):
                    # Can't use the star any more 
                    cache[(i, j)] = False
                    return False
                if j-1 >= 0 and (s[i] == p[j-1] or p[j-1] == '.'):
                    # Keep using the star
                    matched = matched or dfs(i+1, j)
                    if not matched:
                        # Stop using the star
                        matched = matched or dfs(i+1, j+1)
                    cache[(i, j)] = matched
                    return matched
                else:
                    cache[(i, j)] = False
                    return False
            
            # Check for *
            if j+1 < len(p) and p[j+1] == '*':
                # Skip the starred char
                matched = matched or dfs(i, j+2)
                if not matched:
                    # Use the starred char
                    matched = matched or dfs(i, j+1)
                cache[(i, j)] = matched
                return matched
            else:
                # No star in p next
                if i == len(s):
                    # Can't use the star any more 
                    cache[(i, j)] = False
                    return False
                if s[i] == p[j] or p[j] == '.':
                    matched = dfs(i+1, j+1)
                    cache[(i, j)] = matched
                    return matched
                else:
                    cache[(i, j)] = False
                    return False
        return dfs(0, 0)
                
        