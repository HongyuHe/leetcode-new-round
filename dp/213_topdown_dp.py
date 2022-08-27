class Solution:
    def rob(self, nums: List[int]) -> int:
        # [4,3,1,3]
        def rob_the_rest(start, houses):
            if start >= len(houses):
                return 0
            
            if cache[start] >= 0:
                return cache[start]
            
            if start == len(houses)-1:
                cache[start] = houses[-1]
                return houses[-1]
            
            money = max(
                houses[start] + rob_the_rest(start+2, houses),
                rob_the_rest(start+1, houses),
            )
            cache[start] = money
            return money
        
        cache = [-1] * len(nums)
        rob_first = nums[0] + rob_the_rest(2, nums[:-1])
        
        cache = [-1] * len(nums)  #* Clear the cache!!!
        rob_no_first = rob_the_rest(1, nums)
        
        amount = max(
            rob_first,
            rob_no_first,
        )
        return amount
        