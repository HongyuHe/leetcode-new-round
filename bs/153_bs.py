class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## 1) Find the pivot.
        ## 2) Return left-most element of the smaller part.
        ## [3,4,5,6,7,8,1,2]
        ## [1,2,3]
        ## [2,3,1]
        ## [2,3,0,1]
        
        l, r = 0, len(nums)-1
        pivot = 0
        while l < r:
            if l+1 == r and nums[l] > nums[r]:
                pivot = r
                break
            
            m = (l+r) // 2
            if nums[l] > nums[m]:
                r = m
            elif nums[m] > nums[r]:
                l = m
            else:
                # * Sorted 
                break
        return nums[pivot]
                
                
            
            
            
                        