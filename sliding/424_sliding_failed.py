class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #* Translates to finding the longest contiguous substring
        #* with k replacements.
        #* Method sketch: 
        #* -- Two pointers l and r starting from 0
        #* -- Move r until encounting a different letter
        #* -- Replace => k--
        #* -- Repeat until k==0
        #* -- Record the length
        #* -- Move l to the first location at which the letter was replaced 
        #* -- Reset k; Repeat the above
        #* => Worst case: alternating -> O(n)
        #! BUT there can be >2 kinds of characters!!!
        if len(s) == 1:
            return 1

        l, r = 0, 1
        budget = k
        longest = -1
        first_idx = -1
        
        tmp_s = s
        while r < len(s):
            if tmp_s[l] == tmp_s[r]:
                r += 1
                if r == len(s):
                    #* Reached the end.
                    longest = max(r-l, longest)
            else:
                if budget:
                    if first_idx < 0:
                        first_idx = r
                    #* Replace the current char with the previous
                    tmp_s = tmp_s[:r] + tmp_s[l] + tmp_s[r+1:]
                    #* Deduct the budget
                    budget -= 1
                    r += 1
                    if r == len(s):
                        #* Reached the end.
                        longest = max(r-l, longest)
                else:
                    longest = max(r-l, longest)
                    if first_idx > 0:
                        l = first_idx
                    else:
                        #* Don't get to replace any char (k == 0)
                        l = r
                    r = l + 1
                    #* Reset
                    tmp_s = s
                    first_idx = -1
                    budget = k
        return longest
        #TODO: Special case: replacing the first char, e.g., "ABBB"


