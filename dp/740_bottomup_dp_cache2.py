class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # * Deleting one number == deleting all numbers of the same value.
        # * Dedupe -> build a dict to keep track of counts.
        from collections import Counter
        # * Example: [2,2,3,3,3,4] -> [2 3 4] 
        # * => [0, 2] => [2*2, 0+3*3, max(2*2 + 4, 3*3)] => [4, 9, 9] => 9 (here we have the full cache).
        counter = Counter(nums) 
        choices = sorted(list(set(nums)))
        # * Max. value can be earned by index (i-1) and (i-2).
        # * Base case, only need to keep two previous choices.
        cache = [0, 0]

        for i in range(len(choices)):
            num = choices[i]
            take_sum = counter[num] * num
            if choices[i-1] == num-1:
                take_sum += cache[0]
            else:
                take_sum += cache[1]

            notake_sum = cache[1]
            
            # * Update the cache with the best decision.
            cache[0] = cache[1]
            cache[1] = max(take_sum, notake_sum)

        return cache[1]
