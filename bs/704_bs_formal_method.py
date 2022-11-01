'''
Critcical edge case: len(nums)==2
    * If `m` takes the floor, i.e., m = (l+r) // 2: 
'''
class Solution:
    def search(self, nums, target: int) -> int:
        l, r = 0, len(nums)-1

        #%assert loop invariant
        while l < r:
            #%assert nums[<l]: < target & nums[>=r]: >= target 
            m = (l+r) // 2
            
            if target > nums[m]:
                l = m + 1
            else:
                r = m
                
        return l if nums[l] == target else -1
        
         