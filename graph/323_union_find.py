class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """ 24min failed.
        Plan: Union find
            * Initiate parents of all nodes as themselves.
            * After union find, check # of unique parents.
        """
        parents = [i for i in range(n)]
        #* Track total components. We start with n.
        self.components = n
        
        def find(node: int) -> int:
            parent = parents[node]
            if parent == node:
                return node

            #* Path compression
            parents[node] = find(parent)
            return parents[node]
        
        def union(i: int, j: int):
            parent_i = find(i)
            parent_j = find(j)

            if parent_i == parent_j:
                #* This's cycle -> in the same component -> do nothing
                return
            
            #! BUG: Link their roots! (not the original nodes)
            # if parent_i < parent_j:
            #     parents[j] = parent_i
            # else:
            #     parents[i] = parent_j

            #^ Fixed (also, no need to check the ordering)
            parents[parent_j] = parent_i
            
            #* Optimization:
            #* Every successful merge reduces total components by 1
            self.components -= 1
            return 
        
        for i, j in edges:
            union(i, j)
        # roots = set()
        # for node in range(n):
        #     roots.add(find(node))
        # return len(set(roots))
        return self.components

