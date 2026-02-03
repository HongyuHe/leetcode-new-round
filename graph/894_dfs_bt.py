# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        """
        Recursive search:
            * Given n, try all possible left and right splits 
            * Return when ≤2 nodes
            * Caching afterward
        """
        cache = {}

        def _dfs(remaining):
            if remaining in cache:
                return cache[remaining]
            if remaining == 1:
                return [TreeNode()]
            if remaining == 2:
                return []
            
            #* Subtract the root node.
            remaining -= 1
            trees = []
            for num_left in range(1, remaining):
                num_right = remaining - num_left

                ltrees = _dfs(num_left)
                if ltrees is None: continue
                rtrees = _dfs(num_right)
                if rtrees is None: continue

                for ltree in ltrees:
                    for rtree in rtrees:
                        root = TreeNode()
                        root.left = ltree
                        root.right = rtree
                        trees.append(root)
            cache[remaining+1] = trees
            return trees
        return _dfs(n)
