class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False

        target = total // 2
        memo = {}
        get_key = lambda i, g: f"{i}-{g}"
        
        def can_partition(index, goal):
            key = get_key(index, goal)
            if key in memo.keys(): return memo[key]

            if goal == 0:
                # * Base case 1: The target has been achieved before using the subarray nums[:index]
                return True
            if index == 0:
                # * Base case 2: The only way to achieve the goal when 
                # * the subarry in consideration has a sinlge element.
                return nums[0] == goal
            
            take_this = can_partition(index-1, goal - nums[index]) if goal >= nums[index] else False
            dont_take_this = can_partition(index-1, goal)

            result = take_this or dont_take_this
            memo[key] = result
            return result

        return can_partition(len(nums)-1, target)
