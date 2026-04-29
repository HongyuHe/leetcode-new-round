class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """ 24 min, fixed a bug with AI
        Plan: Union find
            * Each node is the parent of itself at init.
            * Union nodes on the two ends of an edge by setting one of them as the parent of the other.
                * During the union, if two nodes are already of the same origin -> cycle
            * At the end, all nodes should have the same parent, otherwise disconnected
        """
        # from collections import defaultdict
        parents = [node for node in range(n)]
        sizes = [1] * n

        def find(node):
            parent = parents[node]
            if parent == node:
                return parent
            else:
                return find(parent)
        
        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return False
            
            sizes[pa] += sizes[pb]
            parents[pb] = pa
            return True
        
        for a, b in edges:
            if not union(a, b):
                # print(parents)
                return False
        
        #* Deal with disconnected graphs
        # print(sizes)
        return max(sizes) == n
        