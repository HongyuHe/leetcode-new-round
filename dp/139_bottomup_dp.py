class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Example: "applepenapple"
        cache = [False] * (len(s)+1)
        cache[-1] = True

        # * O(N*M) where len(wordDict)==M.
        for i in range(len(s)-1, -1, -1):
            substr = s[i:]
            for word in wordDict:
                l = len(word)
                if l <= len(substr) and word == substr[:l] and cache[i+l] == True:
                    cache[i] = True
                    break
        return cache[0]
