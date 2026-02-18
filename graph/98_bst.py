# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Can a BST have duplicate values? If so, how to deal with them?
        Is a full BST?

        Plan:
            * Recursion -- validate the subtrees bottom up
        """
        def dfs(node) -> (bool, (int, int)):
            isleft_valid, (lmin, lmax) = (
                dfs(node.left) if node.left else (True, (node.val, node.val))
            )
            isright_valid, (rmin, rmax) = (
                dfs(node.right) if node.right else (True, (node.val, node.val))
            )

            if isleft_valid and isright_valid:
                if (node.left and lmax >= node.val):
                    return False, (0,0)
                if (node.right and rmin <= node.val):
                    return False, (0,0)
            else: 
                return False, (0,0)
            
            #* Propagate the left min and right max from the leaves to the top.
            return True, (lmin, rmax)
        
        return dfs(root)[0]
