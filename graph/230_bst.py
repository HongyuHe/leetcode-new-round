# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """26min, stipped up a bit."""
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Plan:
            ~~1. Traverse the left branch all the alway to the bottom.~~ <- This's sooo wrong.
            1. In order traversal
            2. Backtrack k steps to get the k-th smallest.
        """
        kth_smallest = None
        rank = k
        def dfs(node):
            nonlocal kth_smallest
            nonlocal rank

            if not node:
                return
            
            dfs(node.left)
            #* Traverse the current node.
            if not kth_smallest:
                rank -= 1
                if rank == 0:
                    kth_smallest = node.val
            dfs(node.right)
            return
        
        dfs(root)
        return kth_smallest         
