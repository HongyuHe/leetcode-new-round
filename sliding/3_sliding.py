class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## Two pointers
        ## pwwkew
        ## abcabcbb
        
        
        if len(s) <= 1:
            return len(s)
        
        low, high = 0, 1
        longest = 1
        while high < len(s):
            subs = s[low:high+1]
            if s[high] == s[high-1]: # * Not necessary, but just for marginal performance.
                low = high
                high += 1
            elif len(set(subs)) < len(subs):
                low += 1
            else:
                longest = max(longest, len(subs))
                high += 1
            # print(s[low:high+1])
        
        return longest