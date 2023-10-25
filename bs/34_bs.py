class Solution:
    def searchRange(self, nums: List[int], target: int) :
        #* Use binary search to the start -> expand in both directions
        #* Example: [5,7,7,8,8,10], target=8
        #*  l=0, r=5, m=2 -> mid=7 < target 
        #*  l=3, r=5, m=4 -> mid=8 == target
        #* When moving pointer, take into account duplicates. 
        
        length = len(nums)
        if not length:
            return [-1, -1]
        
        l = 0
        r = length - 1
        while l <= r:
            m = (l+r) // 2
            print(f"{(l, m, r)=}")
            if target < nums[m]:
                r = m - 1
                #! No need to dedupe (much slower)
                # while r-1 >= 0 and l <= r-1 and nums[r] == nums[r-1]:
                #     #* Dedupe
                #     r -= 1
                    
            elif target > nums[m]:
                l = m + 1
                #! No need to dedupe (much slower)
                # while l+1 < length and l+1 <= r and nums[l] == nums[l+1]:
                #     #* Dedupe
                #     l += 1
            else:
                #* Found the target
                break
        
        #* Target not found.
        if nums[m] != target:
            return [-1, -1]

        #* Expand to locate the range.
        end = m
        for i in range(m+1, length):
            if nums[i] == target:
                end += 1
            else:
                break

        start = m
        for i in range(m-1, -1, -1):
            if nums[i] == target:
                start -= 1
            else:
                break
        return [start, end]

                

        


