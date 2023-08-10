class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        # * Goal: Maximize the minmum value while keeping the sum large.
        # * Method: Try monotonic increasing stack.
        # * -- Pop upon a smaller value, and compute the max.
        # * -- Record the starting position of the subarray (default end position to the end).
        # * -- Cache the sum of subarraies -> compute sum in O(1)
        # * Example: [1,2,3,2] -> {1: 0, 2: 1, 3: pop(3*3), 2: 3(?)}
        # * Example2: [2,3,3,1,2] -> {2: 0, 3: 1, 3: 2, 1: pop} => max: 3 -> 3*(3+3)=18 -> 2*(2+3+3)=16 => 18
        # *             {1: 3, 2: 4} pop => max: 2*2 -> 1 * (1+2) < 18

        # * Initialize with a 0 for convenience in indexing.
        prefix_sums = [0]
        # * A list of tuples (val, start pos).
        inc_stack = [] 

        max_sum = -1
        prev_num = -1
        total = 0
        for i, num in enumerate(nums):
            cur_start = i
            if num >= prev_num:
                # * In increasing order.
                inc_stack.append( (num, i) )
            else:
                # * Start popping out until a smaller number.
                # * This marks the end of an increasing subarray.
                n, start = inc_stack.pop()
                while n > num:
                    subsum = (prefix_sums[i] - prefix_sums[start])
                    cur_sum = n * subsum
                    max_sum = max(cur_sum, max_sum)
                    cur_start = start
                    
                    if inc_stack:
                        n, start = inc_stack.pop()
                    else:
                        # * Empty stack.
                        break
                    
                if n <= num:
                    # * Put it back since n>num (popped one more).
                    # * Add the current number with `start` expanded to the left+1.
                    inc_stack.append( (n, start) )
                
                # * Add the current number.
                inc_stack.append( (num, cur_start) )

            prev_num = num
            # * Compute prefix sums.
            total += num
            prefix_sums.append(total)
        
        # * Remaining elements all have end position at the end.
        while inc_stack:
           # * Start popping out until a smaller number.
            n, start = inc_stack.pop()
            cur_sum = n * (total - prefix_sums[start])
            max_sum = max(cur_sum, max_sum)

        return max_sum % int(1e9 + 7)


