class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """ 29min, one successful attempt
        Graph traversal problem --- Nodes: letters, Levels: numbers

        Plan:
            * Build the graph given `digits`
            * DFS with backtracking to get all the paths
        """
        import string
        chars = string.ascii_lowercase

        layers = []
        for digit in digits:
            letters = ''
            match digit:
                case '7':
                    letters = 'pqrs'
                case '8':
                    letters = 'tuv'
                case '9':
                    letters = chars[-4:]
                case _:
                    start = (int(digit) - 2) * 3
                    letters = chars[start:start+3]
            layers.append(list(letters))
        
        #* Issues: repeated letters -> repeated work?
        combos = set()
        def dfs(lvl, combo):
            if lvl == len(layers):
                combos.add(combo)
                return
            for char in layers[lvl]:
                dfs(lvl+1, combo+char)
        
        dfs(0, '')
        return list(combos)