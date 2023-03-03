class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def two_sum(nums, target):
            if len(nums)<2: return []

            high = len(nums) - 1
            low = 0
            prev = None
            results = []
            while low < high:
                # * Dedupe
                if nums[low]==prev:
                    low += 1
                    continue

                total = nums[low] + nums[high]
                if total==target:
                    results.append([nums[low], nums[high]])
                    prev = nums[low]
                    high -= 1
                    low += 1

                elif total>target:
                    high -= 1
                else:
                    low += 1
            return results

        def k_sum(k, nums, target):
            if len(nums)<k: return []
            
            # * Base case
            if k==2:
                return two_sum(nums, target)

            results = []
            for i in range(len(nums)-k+1): # * +1 for len(nums)==k.
                if i>0 and nums[i]==nums[i-1]: 
                    continue

                new_target = target - nums[i]
                # * The following deals with all possible cases where nums[i] is selected.
                # * -> we don't need to consider it anymore (i.e., NOT ``nums[:i]+nums[i+1:]``)
                result = k_sum(k-1, nums[i+1:], new_target)
                if result:
                    results += [ls+[nums[i]] for ls in result]

            return results
        
        # * Sort the values
        nums.sort()
        # * Invocation
        return k_sum(4, nums, target)
        