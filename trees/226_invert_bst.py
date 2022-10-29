# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        while queue:
            ## Pop the next node
            node = queue[0]
            queue = queue[1:]
            if not node: continue
            
            queue.append(node.left)
            queue.append(node.right)
            ## Swape
            node.left, node.right = node.right, node.left
        return root            
            
            
#         if len(root)==0: return root
        
#         level = 1
#         start = 1
#         while start < len(root):
#             num_nodes = 2**level
#             end = min(len(root), start+num_nodes)
#             level_set = root[start: end]
#             root = root[: start] + reversed(level_set) + root[end: ]
#             start = end
#         return root