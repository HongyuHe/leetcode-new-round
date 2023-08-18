class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # * Example: [1,2,2]
        # * powerset=[[1, 2, 2]]
        # * powerset=[[1, 2, 2], [1, 2]]
        # * powerset=[[1, 2, 2], [1, 2], [1]]
        # * powerset=[[1, 2, 2], [1, 2], [1], [2, 2]]
        # * powerset=[[1, 2, 2], [1, 2], [1], [2, 2], [2]]
        # * powerset=[[1, 2, 2], [1, 2], [1], [2, 2], [2], []]
        # * Sorting to dedupe.
        nums.sort()
        powerset = []
        used = [False] * len(nums)
        
        def traverse(idx, subset):
            if idx >= len(nums):
                powerset.append(subset.copy())
                return

            num = nums[idx]
            if idx > 0 and not used[idx-1] and nums[idx-1] == num:
                # * The previous num was skipped and is the same as the current one,
                # * meaning that the other branch (that used this `num`) will cover 
                # * all cases containing ≥1 `num` -> prune this branch.
                return traverse(idx+1, subset)
            
            # * Taking `num`:
            used[idx] = True
            subset.append(num)
            traverse(idx+1, subset)
            
            # * Not taking `num`:
            # * Backtracking.
            subset.pop()
            used[idx] = False
            traverse(idx+1, subset)

            return
        
        traverse(0, [])
        return powerset
    