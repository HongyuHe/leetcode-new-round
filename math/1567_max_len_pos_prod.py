class Solution(object):
    def getMaxLen(self, nums):
        """
        * Keep both the negative and positive lengths,
         since upon a negative number, the negative length turns 
         into positive length (the solution).
        * Similar to the DP problem in which you keep both neg and pos 
         values to compute the recurrence.
        """
        pos_len = neg_len = longest = 0

        for num in nums:
            if num > 0:
                #* pos x pos = pos
                pos_len += 1
                #* neg x pos = neg (if there was a neg)
                neg_len += 1 if neg_len else 0
            elif num < 0:
                #* Upon a neg number:
                #* neg x neg = pos (neg length turns into pos length if there was a neg)
                #* pos x neg = neg (pos length turns into neg length)
                pos_len, neg_len = neg_len + 1 if neg_len else 0, pos_len + 1
            else:
                #* num == 0
                #* Check in result
                longest = max(pos_len, longest)
                #* Clear counters
                pos_len = neg_len = 0
        
            longest = max(pos_len, longest)
        
        return longest