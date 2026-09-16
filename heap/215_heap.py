class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        nums = [n*-1 for n in nums]
        heapq.heapify(nums)
        while k:
            res = heapq.heappop(nums)
            k -= 1
        return -res