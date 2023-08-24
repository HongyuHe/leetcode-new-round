class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # * Example: "aabba": [a]->[a]: T, [a,b]: F, [a,b,b]: F, [a,b,b,a]: T
        results = []
        
        def is_palindrome(subset):
            l = len(subset)
            for i in range(l // 2):
                if subset[i] != subset[l-1-i]:
                    return False
            return True

        def dfs(remaining, partition):
            if not remaining:
                # * Found a valid solution.
                results.append(partition)
                return 
            
            for end in range(1, len(remaining)+1):
                subset = remaining[:end]
                if is_palindrome(subset):
                    # * Add the palindrome string(!) to the partition.
                    partition.append(''.join(subset))
                    # * Pass a copy of it.
                    dfs(remaining[end:], partition[:])
                    # * Backtracking
                    partition.pop()
            return
        
        dfs(list(s), [])
        return results
