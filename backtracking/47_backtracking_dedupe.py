class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        # * Sorting for dedupe.
        nums.sort()

        def dfs(remaining, perm):
            if not remaining:
                results.append(perm[:])
                return
            
            rest = remaining[:]
            prev_num = -11
            for i, num in enumerate(remaining):
                if num == prev_num:
                    # * Skip duplicates.
                    continue
                
                rest.remove(num)
                perm.append(num)
                # ! Use the copy of the `perm`, which will be modified.
                dfs(rest, perm[:])
                # * Backtracking:
                # ! Appending will mess up the ordering!
                # rest.append(num)
                # * Inserting will preserve the ordering s.t. we don't need to sort every time.
                rest.insert(i, num)
                perm = perm[:-1]

                prev_num = num
            return

        dfs(nums, [])
        return results
