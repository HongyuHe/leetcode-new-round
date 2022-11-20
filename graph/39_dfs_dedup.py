class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ## candidates = [2,3,6,7], target = 7
        ## [2]: [2,2,3] [3,3,3] [3,6,7]
        ## Input: candidates = [2,3,5], target = 8


        def dfs(subset, diff):
            # * Run out of candidates.
            if not subset or diff < 0: return []                
        
            results = []
            for i, n in enumerate(subset):
                cur_diff = diff - n
                if cur_diff == 0:
                    # * Found a solution.
                    results.append([n])
                else:
                    # * Avoid duplication.
                    # * The subset contains the current number `n` but not the ones before.
                    result = dfs(subset[i:], cur_diff)
                    if result:
                        results += [[n]+r for r in result]
                
            return results
            
        return dfs(candidates, target)
                    
        