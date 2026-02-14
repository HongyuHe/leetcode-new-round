# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []

        from collections import deque
        queue = deque()

        levels = []
        queue.append(root)
        while queue:
            level = []
            #! Need two queues to keep track of the current level and the next level
            nxtq = deque()
            while queue:
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    nxtq.append(node.left)
                if node.right:
                    nxtq.append(node.right)
            levels.append(level)
            queue = nxtq
        return levels
