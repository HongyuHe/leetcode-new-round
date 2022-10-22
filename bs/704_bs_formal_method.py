class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1

        #%assert loop invariant
        while l < h:
            #%assert nums[<l]: < target & nums[>=h]: >= target 
            m = (l+h) // 2
            
            if nums[m] < target:
                l = m + 1
            else:
                h = m
                
        return l if nums[l] == target else -1
            
        