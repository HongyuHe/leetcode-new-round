class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        import copy
        power_set = [[]]
        for num in nums:
            new_set = copy.deepcopy(power_set)
            # * Taking the number.
            for s in power_set:
                s.append(num)
                new_set.append(s)
            # * Not taking by adding previous numbers.
            power_set = new_set
        return power_set
