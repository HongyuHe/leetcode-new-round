# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ## `preorder` (root, left, right) -> 1st is the root
        ## `inorder`  (left, root, right) -> use the root to find the lengths of left and right -> `preorder`
        ## preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
        ## preorder = [3,9], inorder = [9,3]
        def build_tree(preorder, inorder):
            # print(preorder, inorder)
            if len(preorder) == len(inorder) == 1:
                return TreeNode(val=preorder[0])
            elif not preorder and not inorder:
                return None
            
            root = TreeNode()
            root.val = preorder[0]
            
            split = inorder.index(root.val)
            left_len = split - 0
            # right_len = len(inorder) - split
            
            root.left  = build_tree(preorder[1: left_len+1], inorder[: split])
            root.right = build_tree(preorder[left_len+1:], inorder[split+1: ])  
            return root
        
        return build_tree(preorder, inorder)
        
        
        