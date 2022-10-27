class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## LB: -(-sum(piles) // h); UB: -(-max(piles) // h) * len(piles) 
        ## Binary search: get speed -> compute time -> Compare with h: go L/R -> time==h or boundary: Stop
        
        lb = -(-sum(piles) // h)
        ub = -(-max(piles) // (h // len(piles))) ## ceil==-(-a//b)
        if len(piles) == 1: return lb
        if min(piles) == max(piles): return ub

        while ub > lb:
            m = (ub+lb) // 2
            
            ## Compute the total time needed.
            time = 0
            for pile in piles:
                time += -(-pile//m)
            
            # print('\t', time, h)
            if time <= h:
                ## Too fast.
                ub = m
            else:
                #%| time > h
                lb = m+1
            
        
        #%| m -> time <= h; s in speeds: s < m -> >time; m < s -> <time
        return ub