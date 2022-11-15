class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## Build a hash table for `s`: letter -> 0
        ## Hash `t` to the table: if exist -> 1
        if len(s) != len(t): return False
        
        table = {}
        
        for c in s:
            counter = table.get(c, 0)
            table[c] = counter + 1
        # print(table)
        for c in t:
            counter = table.get(c, -1)
            if counter <= 0:
                return False
            else:
                table[c] = counter-1
        # print(table)
        return True
            
