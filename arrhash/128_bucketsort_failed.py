class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #! TLE at 72 / 74
        #* Quasi-bucket sort
        #* Time: O(n); Space: O(n)
        if not nums: 
            #* Empty sequences
            return 0

        end = max(nums)
        numbers = set(nums)
        length = len(numbers)

        longest = 0
        counter = 1 #* Initialize to one.
        num = min(nums)
        while num <= end:
            num += 1
            if num in numbers:
                counter += 1
            else:
                longest = max(longest, counter)
                if longest >= length / 2:
                    #* The remaining numbers can form a longer sequence than the current `longest`.
                    break
                #* Clear the counter to zero.
                counter = 0
            
        return longest
