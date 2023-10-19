class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #* Quasi-bucket sort
        #* Time: O(n); Space: O(n)
        if not nums: 
            #* Empty sequences
            return 0

        end = max(nums)
        numbers = set(nums)
        length = len(numbers)

        #* Find all the starting positions
        #^ Don't be afraid of doing linear scans to collect more info
        starts = set()
        for n in numbers:
            #* No left position -> start
            if n-1 not in numbers:
                starts.add(n)

        longest = 0
        counter = 0
        for num in starts:
            n = num
            counter += 1
            while n+1 in numbers:
                counter += 1
                n += 1
            
            longest = max(counter, longest)
            counter = 0
        return longest
