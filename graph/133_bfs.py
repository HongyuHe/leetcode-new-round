"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """ 40min, fixed by AI. Need a 2nd round
        Goal: Traverse all nodes and edges only once

        Plan:
            * Use BFS for traversal
            * Clone nodes as we go, marking visted nodes to prevent redundant visits
        """
        if not node:
            return None

        from collections import deque
        from copy import deepcopy
        clone = Node(val=1)
        queue = deque([node])
        visited = set([1])
        #* index -> Node
        copies = {1: clone}

        while queue:
            n = queue.popleft()
            cp = copies[n.val]
            for neighbor in n.neighbors:
                if neighbor.val not in copies:
                    copies[neighbor.val] = Node(val=neighbor.val)
                    queue.append(neighbor)
                cp.neighbors.append(copies[neighbor.val])
        return clone
