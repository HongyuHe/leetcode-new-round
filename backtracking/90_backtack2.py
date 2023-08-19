class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # * Example: [1,2,2]
        # * powerset=[[1, 2, 2]]
        # * powerset=[[1, 2, 2], [1, 2]]
        # * powerset=[[1, 2, 2], [1, 2], [1]]
        # * powerset=[[1, 2, 2], [1, 2], [1], [2, 2]]
        # * powerset=[[1, 2, 2], [1, 2], [1], [2, 2], [2]]
        # * powerset=[[1, 2, 2], [1, 2], [1], [2, 2], [2], []]
        
        # * Still need sorting to dedupe, otherwise requires adding permutations.
        nums.sort()
        added = set()
        powerset = []

        def traverse(idx, subset):
            if idx >= len(nums):
                uid = '-'.join([str(n) for n in subset])
                if uid not in added:
                    added.add(uid)
                    powerset.append(subset.copy())
                return

            num = nums[idx]

            # * Taking `num`:
            subset.append(num)
            traverse(idx+1, subset)
            
            # * Not taking `num`:
            # * Backtracking.
            subset.pop()
            traverse(idx+1, subset)
            return
        
        traverse(0, [])
        return powerset