class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        idx = -1

        while l <= r:
            ##* Take ceiling:
            m = -(-(l+r) // 2)
            ##* Or floor (doesn't matter -> robust)
            # m = (l+r) // 2
            if nums[m] == target:
                idx = m
                break
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
                
        return idx
            
        