# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Notes:
        * We can only split once at a node, and no split after the top node.
        * Nodes can have negative values.

        Plan: 
        * DFS 
        * For each node, 
            * compute the max sum if split at this node.
            * the max path sum without splitting for propagating upward.
        """
        #* Max path sum when splitting at any node
        pathsum_max = -1000 - 1
        # #* Node -> path sum without splitting
        # pathsums = {}

        def dfs(node: TreeNode) -> int:
            nonlocal pathsum_max
            if not node:
                return 0
            
            left_pathsum = dfs(node.left)
            right_pathsum = dfs(node.right)

            pathsum = node.val + left_pathsum + right_pathsum
            pathsum_max = max(pathsum_max, pathsum)
            return max(0, 
                #* Don't take it if < 0
                node.val + max(left_pathsum, right_pathsum))
        
        dfs(root)
        return pathsum_max
    