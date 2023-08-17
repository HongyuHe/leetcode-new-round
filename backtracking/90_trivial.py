class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        import copy

        # * Sort the numbers, making ordering irrelevant.
        nums.sort() # * O(N logN)
        power_set = [[]]
        added = set()

        for num in nums:
            new_set = copy.deepcopy(power_set)
            for s in power_set:
                s.append(num)
                uid = '-'.join([str(n) for n in s])
                if uid in added:
                    # * Dedupe.
                    continue
                else:
                    added.add(uid)
                    new_set.append(s)
            power_set = new_set
        return power_set