class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1]*len(nums)
        
        def rob_the_rest(start):
            if start >= len(nums): return 0
            
            #* Memorisation.
            if cache[start] >= 0:
                return cache[start]
            
            #* Base case.
            if start == len(nums)-1:
                cache[-1] = nums[-1]
                return nums[-1]
            
            #* Recurrence relation.
            amount = max(
                rob_the_rest(start+1),  #* Skip this house and take the max of the rest.
                nums[start] + rob_the_rest(start+2),  #* Rob this one and skip the next.
            )
            cache[start] = amount
            return amount
        
        return rob_the_rest(0)