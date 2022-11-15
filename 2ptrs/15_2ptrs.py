class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## Sort `nums`: unique (pos1 pos2 pos3) -> O(nlgn)
        ## Use two ptrs: shrink to find pos2 pos3
        ## [-1,0,1,2,-1,-4]
        ## [-4,-1,-1,-1,0,1,2,2]
        ## [1,2,-2,-1]
        ## [-2,-1,1,2]
        
        nums.sort()
        prev = None
        result = []
        for i, n in enumerate(nums):
            if n == prev: 
                # * Avoid duplications.
                continue
            target = -n
            
            # ! Always get the following wrong :|
            l, r = i+1, len(nums)-1
            while l < r:
                total = nums[l] + nums[r]
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    # * Found a unique solution.
                    result.append([n, nums[l], nums[r]])
                    # * Move the two ptrs to the next unique place.
                    # ! Quite ugly.
                    old = nums[l]
                    while l < r and nums[l] == old:
                        l += 1
                    old = nums[r]
                    while l < r and nums[r] == old:
                        r -= 1
            prev = n
            #> l==r
        return result