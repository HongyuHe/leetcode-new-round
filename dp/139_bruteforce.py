class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ## 1) Repeatly find the indices of the words in the dict -- 300K 
        ## 2) Order those indices to form `s`.
        ## s = "leetcode", wordDict = ["leet","code"]
        ## [0, 3] [4, 7] -> [0, 7]
        ## s = "applepenapple", wordDict = ["apple","pen"]
        ## [0, 4] `find('apple', 4) [8, 12] [5, 8]
        ## [0, 4][5, 7][8, 12]
        ## s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
        ## [0, 4] [6, 9] [3, 7] [4, 7] [0, 2]
        ## [0, 2] [3, 7] [4, 7] [6, 9] X
        ## [0, 4] [3, 7] [4, 7] [6, 9] X
        
        indices = []
        for word in wordDict:
            prev_index = -1
            while True:
                index = s.find(word, prev_index+1)
                if index >= 0:
                    indices.append( (index, index+len(word)) )
                    if index == prev_index:
                        # * Found all occurrences
                        break
                else: 
                    # * Not found
                    break
                prev_index = index
        
        indices.sort()
        
        
        nxt_pos = set([0])
        old_pos = 0
        for pair in indices:
            start, end = pair
            if start not in nxt_pos:
                if start == old_pos:
                    # * Repeated token.
                    nxt_pos.add(end)
                else:
                    # * Discontiguous path.
                    # * Try the next one.
                    continue
            else:
                # * Contiguous path.
                # nxt_pos.clear() # ! Do NOT clear the path -> add all possible routes/
                nxt_pos.add(end)
                old_pos = start
        if len(s) in nxt_pos:
            return True
        
        return False
        