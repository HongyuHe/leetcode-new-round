class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
      # * DP: Subproblem is the prefix arraries.
      # Example: [1,1,1,1,1]
      # [1] -> {-1, 1}
      # [1,1] -> {-2: 1, 0: 2, 2: 1}
      # [1,1,1] -> {-3: 1, (-1: 1, -1: 2), (1: 2, 1: 1), 3: 1} 
      #         -> merge entries: {-3: 1, -1: 3, 1: 3, 3: 1}
      # [1,1,1,1] -> {-4: 1, (-2: 1, -2: 3), (0: 3, 0: 3), (2: 3, 2: 1), 4: 1}
      #         -> merge entries: {-4: 1, -2: 4, 0: 6, 2: 4, 4: 1}
      # [1,1,1,1,1] -> {-5: 1, (-3: 1, -3: 4), -1: 4, -1: 6, (1: 6, 1: 4), (3: 4, 3: 1), 5: 1}
      #         -> merge entries: {-5: 1, -3: 5, -1: 4, -1: 6, 1: 10, 3: 5, 5: 1}

      # * DP cache: {sum -> number of ways to reach this sum}.
      sums_counter = {}
      # * Initialize the base case with the 1st element.
      first = nums[0]
      sums_counter[first] = 1
      sums_counter[-first] = 1
      # * Edge case:
      if first == 0:
        sums_counter[0] = 2

      for num in nums[1:]:
        new_sums_counter = {}
        for total in sums_counter.keys():
          # * Minus sign
          new_sum = total - num
          if new_sum in new_sums_counter:
            new_sums_counter[new_sum] += sums_counter[total]
          else:
            # * Inherent from the previous subproblem
            new_sums_counter[new_sum] = sums_counter[total]

          # * Plus sign
          new_sum = total + num
          if new_sum in new_sums_counter:
            new_sums_counter[new_sum] += sums_counter[total]
          else:
            # * Inherent from the previous subproblem
            new_sums_counter[new_sum] = sums_counter[total]
        
        # * Update the counters
        sums_counter = new_sums_counter

      # * If the targets 
      return sums_counter.get(target, 0)
