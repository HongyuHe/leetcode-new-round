class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False

        target = total // 2
        cols = target + 1
        rows = len(nums)
        memo = [[False]*cols for _ in range(rows)]

        # * targets: 0, 1, 2, 3, ..., 11
        # * index: 0 T  T
        # *        1 T -1
        # *        2 T -1
        # *        3 T -1

        # * Initialize base case
        for index in range(rows):
            memo[index][0] = True
        if nums[0] == target:
            memo[0][nums[0]] = True 

        # print(memo)
        # * Fill the table
        for index in range(1, len(nums)):
            for goal in range(target+1):
                # * Not taking 
                dont_take = memo[index-1][goal]
                # * Take it 
                do_take = memo[index-1][goal-nums[index]] if goal >= nums[index] else False

                memo[index][goal] = dont_take or do_take
                # print(memo)
                # print(f"{memo[index][goal]=}")
        
        return memo[rows-1][cols-1]

