class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## 1) Compute the "prefix" and "suffix"
        ## 2) Aggregate the results
        prefixes = []
        suffixes = []
        
        prefix = 1
        for n in nums:
            prefix *= n
            prefixes.append(prefix)
        # print(prefixes)
            
        suffix = 1
        for n in reversed(nums):
            suffix *= n
            suffixes.insert(0, suffix)
        # print(suffixes)
        
        results = []
        for i in range(len(nums)):
            prefix = prefixes[i-1] if i != 0 else 1
            suffix = suffixes[i+1] if i < len(nums)-1 else 1
            results.append(
                prefix * suffix
            )
        return results
            
