# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        """
        Plan:
            * Traverse the tree
            * Insert the node
        """
        if not root: return TreeNode(val)
        
        parent = None
        node = root
        while node:
            parent = node
            if val < node.val:
                node = node.left
            else:
                node = node.right
        if val < parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        
        return root