class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        def start_robbing(houses):
            # print('houses=', houses)
            prev_prev = 0
            prev = houses[0]
            # print(f"{prev_prev=}, {prev=}")
            for house in houses[1:]:
                robbed = max(house+prev_prev, prev)
                prev_prev = prev
                prev = robbed
                # print(f"{prev_prev=}, {prev=}")
            return prev
        
        return max(
            start_robbing(nums[1:]),
            start_robbing(nums[:-1]),
        )