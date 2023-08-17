class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total = sum(nums)
        if total % k: return False

        target = total // k
        # * Sort numbers for dedup.
        nums.sort(reverse=True)
        # * Track the used numbers.
        used_nums = [False] * len(nums)

        def can_achieve_target(index, total, s):
            # * Reached the bottom of the decision tree.
            if index == len(nums): 
                return False
            # * Constructed all s subsets.
            if s == 0: 
                return True
            
            # ? Skip if the previous number of the same value was skipped???
            # ? NOTE: "The frequency of each element is in the range [1, 4]."???
            if index > 0 and not used_nums[index-1] and nums[index-1] == nums[index]:
                return can_achieve_target(index+1, total, s)
            
            result = False
            used = used_nums[index] 
            # * 1. Use the current number if hasn't been used:
            if not used:
                used_nums[index] = True
                new_total = total + nums[index]
                if new_total == target:
                    # * Found a solution (s-1) -> Start anew (from index 0 while keeping `used_nums`).
                    result = result or can_achieve_target(0, 0, s-1)
                elif new_total < target:
                    # * Keep searching.
                    result = result or can_achieve_target(index+1, new_total, s)
                else:
                    result = False

            # * Backtrack.
            if not used:
                used_nums[index] = False

            # * 2. Do not use the current number.
            # * NOTE: We have to try both decisions.
            result = result or can_achieve_target(index+1, total, s)
            
            return result

        # * Root call: only need to check (k-1) sets.
        return can_achieve_target(0, 0, k-1)
