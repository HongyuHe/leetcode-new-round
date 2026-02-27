class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """ 20min, 3 prior attempts.

        Plan: Union find
            * Initialize an array of predecessors, where each node is the predecessor of itself.
            * Union each node until we encounter two ends of an edge belonging to the same union.

        Complexity
            * Time: 3 x N x logN -> O(NlogN) where N is #nodes
            * Space: N -> O(1)
        """
        predecessors = [n for n in range(len(edges)+1)]

        def find(node: int) -> int:
            nonlocal predecessors

            pred = predecessors[node]
            if pred == node:
                return pred
            return find(pred)
        
        def union(u, v) -> bool:
            nonlocal predecessors

            pred_u = find(u)
            pred_v = find(v)

            if pred_u == pred_v:
                #* Found a circle.
                return False
            else:
                #* Set the root of union containing u as the predecessor of 
                #* the root of the union containing v.
                predecessors[find(v)] = find(u)
                return True

        for (u, v) in edges:
            if not union(u, v):
                return [u, v]
