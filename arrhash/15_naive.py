class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## Naive solution ≈ two sum (#1): hash table + set for deduplication
        ## O(n^2)
        
        result = set()
        for i, n in enumerate(nums):
            hash_table = {}
            target = -n
            for j, x in enumerate(nums[i+1: ]):
                diff = target - x
                if diff in hash_table:
                    index = hash_table[diff]
                    result.add(tuple(sorted([n, x, nums[index]])))
                hash_table[x] = j+i+1
        return result