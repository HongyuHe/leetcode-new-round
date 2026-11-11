class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if sum(nums) < target:
            return 0
        """
        Attempts:
            1. 30min, failed, The Infinite Loop Bug, fixed by removing the if guard.
        Plan:
            * Two pointers: left right
            * right++ when < target
            * left-- when >= target
        """
        left, right = 0, 0
        total = nums[0]
        shortest = float('inf')
        while right < len(nums):
            if total >= target:
                shortest = min(right-left+1, shortest)
                # if left < right:
                total -= nums[left]
                left += 1
            else:
                right += 1
                if right < len(nums):
                    total += nums[right]
        return shortest