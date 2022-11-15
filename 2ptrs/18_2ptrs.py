class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ## nums = [1,0,-1,0,-2,2], target = 0
        ## [-2,-1,0,0,1,2]
        ## -2: [-1,0,0,1,2]
        ## -2,-1: [0,0,1,2] 3
        ## -> [1,2] -> [-1,1,2] -> [-2,-1,1,2]
        
        # * Sort `nums` to avoid duplicaitons --- O(nlogn)
        nums.sort()
        # print(nums)
        
        # * Recursively reduce the problem down to 2 numbers
        def k_sum(remaining, goal, k):
            if len(remaining) < k: return []
            
            results = []
            if k == 2:
                # * Sliding window approach
                low, high = 0, len(remaining)-1
                prev_low = None
                
                while low < high: 
                    if remaining[low] == prev_low: 
                        low += 1
                        continue
                        
                    total = remaining[low] + remaining[high]
                    # print(low, high, remaining, total, goal)
                    
                    if total == goal:
                        results.append([remaining[low], remaining[high]])
                        # ! Only update for avoiding duplication **if it's a solution**.
                        prev_low = remaining[low]
                        low += 1
                        high -= 1
                    elif total > goal:
                        high -= 1
                    elif total < goal:
                        low += 1
                        
            elif k > 2:
                prev_num = None
                for i in range(len(remaining)-k+1):
                    n = remaining[i]
                    # * Avoiding duplications.
                    if prev_num == n: continue
                    # print('Trying ', n)
                    subresults = k_sum(remaining[i+1:], goal-n, k-1)
                    if subresults:
                        for r in subresults:
                            results.append([n] + r)
                    prev_num = n
            else:
                raise RuntimeError('Unreachable')
            
            return results
        
        return k_sum(nums, target, k=4)
                    
                        
