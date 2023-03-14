class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False

        target = total // 2
        # * Sort the array -> NlogN
        # * Create a current sum set for all possible (deduped) sums
        # * Check if the target is in the total  
        # * if the sums all > target, then return False -> < N^2
        # * Example: [1,5,11,5] -> [1,5,5,11], target: 11

        # nums.sort() # ? Why don't we need to sort it?
        partial_sums = set([0]) # * Zero for keeping single elements.
        for num in nums:
            all_is_greater = True
            new_sums = partial_sums.copy()
            for psum in partial_sums:
                new_sum = psum + num
                if new_sum == target:
                    return True
                elif new_sum < target:
                    all_is_greater = False
                
                new_sums.add(new_sum)
            # *> End for
            if all_is_greater:
                return False
            partial_sums = new_sums
        return False
                