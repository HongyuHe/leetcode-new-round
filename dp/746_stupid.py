# This problem doesn't have the optimal structure, i.e., suboptimal leads to global optimal.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_steps = len(cost)
        
        pos = 0
        total_cost_1 = cost[pos]
        while pos < total_steps-2:
            step1 = pos + 1
            step2 = pos + 2
            
            pos = step1 if cost[step1] < cost[step2] else step2
            total_cost_1 += cost[pos]
        
        pos = 1
        total_cost_2 = cost[pos]
        while pos < total_steps-2:
            step1 = pos + 1
            step2 = pos + 2
            
            pos = step1 if cost[step1] < cost[step2] else step2
            total_cost_2 += cost[pos]
        
        pos = total_steps
        total_cost_3 = 0
        while pos > 1:
            step1 = pos - 1
            step2 = pos - 2
            
            pos = step1 if cost[step1] < cost[step2] else step2
            total_cost_3 += cost[pos]
        
        pos = total_steps-2
        total_cost_4 = cost[pos]
        while pos > 1:
            step1 = pos - 1
            step2 = pos - 2
            
            pos = step1 if cost[step1] < cost[step2] else step2
            total_cost_4 += cost[pos]
        

        return min(min(min(total_cost_1, total_cost_2), total_cost_3), total_cost_4)
            
            