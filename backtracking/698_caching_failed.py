class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # * Do recursion to reduce the problem to partition 2 subsets.
        # * Track the numbers used in previous interations.
        def partition_2_subsets(numbers, target):
            # * 0 is the base case.
            totals = set([0])
            new_totals = set()
            # * total: int -> composition: List[int]
            combo_tracker = {0: []}

            for n in numbers:
                # * Two choices: include or not.
                for total in totals:
                    new_total = total + n
                    combo_tracker[new_total] = combo_tracker[total] + [n]

                    if new_total == target:
                        # * Find one solution -> True, used elements
                        return True, combo_tracker[new_total]
                    
                    # * Include n.
                    new_totals.add(new_total)
                    # * `total` is not including `n` by default.
                # * Add new sums.
                totals = totals.union(new_totals)
            # * Solution not found.
            return False, []
        
        nums_total = sum(nums)
        if nums_total % k:
            return False
        target = nums_total // k
        
        # * Only need too check (k-1) subsets.
        for i in range(k-1):
            can_do, used_nums = partition_2_subsets(nums, target)
            if not can_do:
                return False

            for num in used_nums:
                if num != 0:
                    nums.remove(num)

        return True


