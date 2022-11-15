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
                # * Hash table
                table = {}
                prev = None
                for n in remaining:
                    if prev == n: continue
                    diff = goal - n
                    count = table.get(diff, 0)
                    if count > 0:
                        results.append([diff, n])
                        # ! Only update for avoiding duplication **if it's a solution**.
                        prev = n
                    else:
                        table[n] = count+1
                                            
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
