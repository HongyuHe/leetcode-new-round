class Solution:
    def maxArea(self, height: List[int]) -> int:
        #* Brute force: O(n^2)
        largest = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = min(height[i], height[j]) * (j-i)
                largest = max(largest, area)
        return largest