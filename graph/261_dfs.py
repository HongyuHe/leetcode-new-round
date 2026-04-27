class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Plan: Two solutions --- union find or DFS

        DFS: 40minutes, 5 submissions!
            * Build the adjacency list
            * DFS from the roots
        """
        from collections import defaultdict
        adjlist = defaultdict(list)
        for i, j in edges:
            if i == j:
                #* Self loop
                return False
            #* Undirected graph -> symmetric adj matrix
            adjlist[i].append(j)
            adjlist[j].append(i)
        # print(dict(adjlist))

        visited = set()
        def dfs(node, path):
            if node in path:
                #* Found a cycle!
                # print(f"Cycle: {path=} {node=} {visited=}")
                return False
            if node in visited:
                return True
            
            visited.add(node)
            parent = path[-1] if path else None
            path.append(node)
            for child in adjlist[node]:
                if child == parent: 
                    #* Prevent oscillation
                    continue 
                # print(f"Going from {node=} to {child=}, {path=}")
                #! Use a copy!
                if not dfs(child, path.copy()):
                    return False
            #* Backtrack
            path = path[:-1]
            return True
        
        # for node in range(n):
        #     if not dfs(node, []):
        #         return False
        if not dfs(0, []):
            return False
        else:
            return len(visited) == n

