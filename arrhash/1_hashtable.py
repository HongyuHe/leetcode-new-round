class Solution:
    def twoSum(self, nums: List[int], target: int):
        ## Two nums can add to `target` -> guaranteed
        ## (1) Loop through the `nums`
        ## (2) Construct a hash table: num -> index
        ## (3) Check if the difference is in that table
        
        hash_table = {}
        result = []
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash_table:
                j = hash_table[diff] 
                result += [j, i]
                break
            hash_table[n] = i
        return result