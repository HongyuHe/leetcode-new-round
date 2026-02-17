# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Assume no duplicated values? --- "All Node.val are unique."
        Assume node alway exists? --- "p and q will exist in the BST."

        Plan:
            * Traverse the tree getting two paths to p and q, respectively.
            * Dequeue the paths until the last common node, which is the LCA.
        """
        from collections import deque

        def search(node, target, path):
            if not node:
                #! This shouldn't happen, assuming target exists.
                return 
            
            path.append(node)
            if node.val == target:
                return
            
            if target > node.val:
                search(node.right, target, path)
            else:
                search(node.left, target, path)
        
        pathq = deque()
        pathp = deque()
        search(root, p.val, pathp)
        search(root, q.val, pathq)

        lca = root
        while True:
            nodep = pathp.popleft() if pathp else None
            nodeq = pathq.popleft() if pathq else None
            if None in [nodeq, nodep]:
                break
            
            if nodeq is not nodep:
                break
            
            if nodeq is nodep:
                lca = nodep
        return lca