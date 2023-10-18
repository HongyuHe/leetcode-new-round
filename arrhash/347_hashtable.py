class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #* 1. Build a counter map O(n)
        #* 2. Sort the counter map O(mlogm) ≤ O(nlogn) since m ≤ n
        from collections import Counter
        counter = Counter(nums)
        counter_sorted = sorted(counter.items(), key=lambda e: e[1], reverse=True)
        return [e[0] for e in counter_sorted[:k]]
    