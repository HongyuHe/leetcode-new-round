class Solution:
    def climbStairs(self, n: int) -> int:
        # * Base case: 0 -> 1
        # * 1 -> 1
        # * 2 -> 1 + 1 = 2
        # * 3 -> 2(2->1) + 1 = 3
        # count = [0] * (n+1)
        # count[0] = 1
        # count[1] = 1
        if n <= 2: return n
        one_step = 2
        two_steps = 1
        for step in range(3, n+1):
            # ! We only need to retain two previous steps in the recurrence relation.
            # count[step] = count[step-1] + count[step-2]
            cur_step = one_step + two_steps
            one_step, two_steps = cur_step, one_step
        return cur_step