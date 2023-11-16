class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Method: Backtracking (brute force)
        Example: candidates = [2,5,2,1,2], target = 5
            • Sort: [1,2,2,2,5]
            • Move starting point: i=0-4 -> Decision tree
            • Dedupe
                -- Skip: [i] == [i-1]
                -- Only consider: [i: ]
        """
        #* O(NlogN)
        candidates.sort()
        result = []

        #* O(2^N): A binary decisioin tree of height N
        def dfs(idx, combo, total):
            if total == target:
                result.append(combo)
                return
            
            if total > target or idx >= len(candidates):
                return 


            #* For each number, we have two choices
            num = candidates[idx]

            #* 1. Take the current number 
            dfs(idx+1, combo+[num], total+num)
            
            #* 2. Don't take the current number 
            #! If we don't take it now, we shouldn't take it subsequently either
            #! Otherwise, duplication: (1, 2[0], 2[1]), (1, 2[1], 2[2]), etc.
            while idx+1 < len(candidates) and candidates[idx+1] == num:
                idx += 1
            if idx < len(candidates):
                dfs(idx+1, combo, total)
            return
        
        # prev = 999
        # for i, num in enumerate(candidates):
        #     if num == prev:
        #         #* Dedupe
        #         continue
        #     dfs(i+1, [num], num)
        #     dfs(i+1, [], 0)
        #     prev = num
        dfs(0, [], 0)
        return result
            
