class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(target, i):
            for k in range(i, len(nums)):
                if nums[k] > target:
                    not_take = dfs(target, k+1)
                    take = dfs(nums[k], k+1)
                    if take >= not_take:
                        return 1 + take
                    else:
                        return not_take
            return 0
                    
        
        counts = []
        for j in range(len(nums)):
            target = nums[j]
            count = 1
            for i in range(j+1, len(nums)):
                if nums[i] > target:
                    not_take = dfs(target, i+1)
                    take = dfs(nums[i], i+1)
                    if take >= not_take:
                        count += 1 + take
                    else:
                        count += not_take
                    break
            counts.append(count)
        return max(counts)
            