class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)

        if endWord not in wordList:
            return 0
        
        from collections import deque
        #* (word, dist)
        queue = deque([(beginWord, 1)])
        chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            #* Construct the next level on the fly.
            for i in range(len(word)):
                #* Try all the next words, 
                #! instead of comparing `word` with every word in `wordList` which is O(5000).
                for char in chars:
                    if char == word[i]:
                        continue
                    nxtword = word[:i] + char + word[i+1:]
                    if nxtword in wordList:
                        queue.append( (nxtword, dist+1) )
                        #* Prevent cycles
                        wordList.remove(nxtword)
        return 0