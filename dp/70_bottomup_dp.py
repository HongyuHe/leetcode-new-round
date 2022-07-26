class Solution:
    def climbStairs(self, n: int) -> int:
        step_1 = 1
        step_2 = 1
        
        # ..., 3:1+(1+1), 2:1+1, 1:1, 0:1
        # Start from 2 steps away as the first two steps are the base cases.
        for _ in range(2, n+1):
            tmp = step_1 + step_2
            step_2 = step_1
            step_1 = tmp
            
        return step_1