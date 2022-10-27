class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [0] * len(nums)
        
        for j in range(len(nums)-1, -1, -1):
            feasible_paths = []
            for i in range(j+1, len(nums)+1):
                if i < len(nums):
                    #* Check if it's increasing
                    if nums[i] > nums[j]:
                        #* Make use of the optimal structure i.e., optimal solutions
                        #* to the subproblems are globally optimal.
                        feasible_paths.append(cache[i])  
                else:
                    #* Reached the end (base case).
                    feasible_paths.append(0)  
            cache[j] = 1 + max(feasible_paths)
        return max(cache)
                    
                    
