class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """ Optimized version
        """
        if len(edges) != n-1:
            #! A valid tree must have n-1 edges.
            return False

        parents = [node for node in range(n)]

        def find(node):
            parent = parents[node]
            if parent == node:
                return parent
            else:
                #! Path compression
                parents[node] = find(parent)
                return parents[node]
        
        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return False
            
            parents[pb] = pa
            return True
        
        for a, b in edges:
            if not union(a, b):
                return False
        
        #* An undirected graph with (n-1) edges and no cycles is a tree.
        #! No need to check connectivity!
        return True
        