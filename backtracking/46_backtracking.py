class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        def dfs(perm, remaining):
            if not remaining:
                results.append(perm.copy())
                return
            
            rest = remaining.copy()
            for num in remaining:
                rest.remove(num)
                perm.append(num)
                dfs(perm.copy(), rest)
                # * Backtrack:
                rest.append(num)
                perm = perm[:-1]
            return

        remaining = nums.copy() 
        dfs([], remaining)
        return results
