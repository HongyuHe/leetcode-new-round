class Solution:
    def maxArea(self, height: List[int]) -> int:
        #* Two-pointer
        #! Don't understand the optimality model!!!
        lptr = 0
        rptr = len(height) - 1

        largest = 0
        while lptr < rptr:
            lh = height[lptr]
            rh = height[rptr]
            area = min(lh, rh) * (rptr - lptr)
            largest = max(area, largest)

            if lh < rh:
                lptr += 1
            elif lh > rh:
                rptr -= 1
            else:
                #* Two equal heights: check the next position
                #* (length >= 2: within bound always)
                if height[lptr+1] > height[rptr-1]:
                    lptr += 1
                else:
                    rptr -= 1
        return largest 