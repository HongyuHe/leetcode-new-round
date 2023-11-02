class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #* Brute force: O(n^2)
        longest = 0
        for start in range(len(nums)):
            if longest >= len(nums) - start:
                #* Can't get a longer sequence anymore.
                break
            if nums[start] == 0:
                #* The rest would be 0's anyway.
                continue
            
            # prod = 1
            #! Even if avoiding multiplication, it's still TLE.
            neg_count = 0
            for i in range(start, len(nums)):
                if nums[i] < 0:
                    neg_count += 1
                elif nums[i] == 0:
                    break
                
                if neg_count % 2 == 0:
                    longest = max(i - start + 1, longest)
                # prod *= nums[i]
                # if prod > 0:
                #     longest = max(i - start + 1, longest)
                # elif prod == 0:
                #     #* Later, the `start` will be place after this 0.
                #     break
                
        return longest