class Solution:
    def characterReplacement(self, s: str, k: int):
        '''Sliding window [l: r]
        -- Hashmap as a counter
        -- Replace towards the most common char in the window (c)
        -- Valid window contains ≤k chars to replace -> (r-l+1) - c ≤ k
        -- Stop if r >= len
        '''
        if len(s) == 1:
            return 1

        def get_most_freq(counter):
            #* O(26) in O(1)
            freq = -1
            for k, v in counter.items():
                freq = max(freq, v)
            return freq

        from collections import defaultdict
        counter = defaultdict(int)
        counter[s[0]] += 1

        l, r = 0, 1
        longest = -1

        while r < len(s):
            counter[s[r]] += 1
            freq = get_most_freq(counter)
            #* Check window validity:
            num_replace = (r - l + 1) - freq
            if num_replace <= k:
                #* Valid window
                r += 1
            else:
                #* Not enough budget to replace.
                #* Record the current window size:
                longest = max(r - l, longest)
                #* => Shrink the window
                while (r - l + 1) - get_most_freq(counter) > k:
                    counter[s[l]] -= 1
                    l += 1
                #* Once obtained a valid window, move forward.
                r += 1
        return max(longest, r - l)


