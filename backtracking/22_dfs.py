class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """ 33min, on attempt
        n==3:
        <=1, <=2, <=3
        n==N:
        <=1, <=2, <=3, ..., <=N

        There are `n` slots for placing closing brackets.
        Plan:
            * DFS decide at each level the number closing brackets.
        """

        opening = '(' * n
        combos = []

        def dfs(s: str, pos: int, level: int, nbrackets: int):
            if level > n and nbrackets != 0:
                #* Didn't place enought brackets.
                return
            if nbrackets < 0:
                #* Used too many
                return
            if nbrackets == 0:
                if level <= n:
                    #* Used too many
                    return 
                combos.append(s)
                return
            
            #* Allowed number of brackets = the level - # of used brackets
            allowed_num = level - (n-nbrackets)
            for num in range(allowed_num+1):
                newstr = s[:pos] + ')'*num + s[pos:]
                newpos = pos + num + 1
                dfs(newstr, newpos, level+1, nbrackets-num)

        dfs(opening, 1, 1, n)
        return combos

