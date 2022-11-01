class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## Ex: [4,5,6,1,2]
        ## Ex: [6,1,2,3,4,5] -> 6
        ## [l, m] (l, r]
        ## Case 1: [l, m] is sorted, (m, r] is not
        ## Case 2: [l, m] is not sorted, (m, r] is
        
        if len(nums) == 1: return 0 if nums[0]==target else -1
        if len(nums) == 2: 
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else: 
                return -1
        
        ## 1. Search for the pivot: 
        pivot = -1
        l, r = 0, len(nums)-1
        while l<r:
            m = -(-(l+r) // 2)
            # m = (l+r) // 2 
            # print(l, m, r)
            if nums[l] > nums[m]:
                r = m-1
            else:
                l = m
        pivot = l
        # print(pivot)
            
        ## 2. Correct the order:
        nums_old = nums
        nums = nums[pivot+1:] + nums[:pivot+1]
        # print(nums)
        
        ## 3. Search for the target
        l, r = 0, len(nums)-1
        idx = -1
        while l <= r:
            m = (l+r) // 2
            # print(l, m, r)
            if target == nums[m]:
                idx = m
                break
            elif target > nums[m]:
                l = m+1
            else:
                r = m-1
        # print(idx)
        ## Not found
        if nums[idx] != target:
            return -1
        ## For ordered `nums`
        if nums_old[idx] == target:
            return idx
        
        ## Convert to the original position (truely hack)
        offset = len(nums) - pivot - 1
        if idx >= offset:
            idx -= offset
        else:
            idx += len(nums)-offset
        return idx 
            
            
            
            
        