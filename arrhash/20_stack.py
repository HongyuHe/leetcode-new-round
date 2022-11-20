class Solution:
    def isValid(self, s: str) -> bool:
        ## Input: s = "(]"
        ## "([)]{}"
        
        if len(s) % 2: return False
        
        pairs = {
            '(': ')', 
            '{': '}', 
            '[': ']',
        }
        half = len(s) // 2
        stack = []
        
        for c in s:
            if c in pairs.keys():
                # * Open bracket.
                stack.append(c)
            else:
                if not stack:
                    return False
                bracket = stack.pop()
                # * Close bracket.
                if c != pairs[bracket]:
                    return False
                
        return True if not stack else False
    
    