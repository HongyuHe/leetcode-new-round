class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Lessons: I made two mistakes:
            1. Initially, I wanted to detect cycles by finding roots (nodes with indegree == 0) and DFS from them. 
                - Yes, a DAG must have at least one root with indegree == 0 (it can have multiple roots).
                - But some disconnected components may not have roots when they contain cycles.
            2. Use DFS with a tracking set (`path`) to detect back-edges (cycles).
                - This set is different from the `visited` set.
                - It's a per-path set that tracks the nodes currently being explored in the current DFS path. 
                    If we encounter a node that's already in this set, it means we've found a back-edge, indicating a cycle.
                    A node should be removed from this set once we finish exploring all its children, 
                    allowing it to be visited again in different paths without falsely detecting a cycle.
            3. I failed to "memoize" nodes that it has already fully processed and proven to be safe (cycle-free).
                - If we don't check if a node has already been safely visited before recursing into it, the DFS will needlessly traverse 
                    the same subgraphs multiple times if they are reached via different paths, e.g.,
                    0
                   / \
                  1   2
                   \ /
                    3
                   / \
                   ...
                In this example, if we start DFS from node 0, we will visit nodes 1 and 2, and then node 3. 
                If we don't mark node 3 as visited, when we later start DFS from node 1, we will again visit node 3, which is inefficient.
                This makes the complexity from O(V + E) to O(2^V).
        
        Plan: 
            - Build a dependency graph in adj list ([a,b]: a -> b)
            - Find all the roots (in deg == 0) --> This's wrong
            - From each root, DFS to detect cycles
        """
        from collections import defaultdict
        adjlist = defaultdict(list)
        # indegrees = [0] * numCourses
        for a, b in prerequisites:
            adjlist[a].append(b)
        #     indegrees[b] += 1
        
        # roots = [a for a in range(numCourses) if indegrees[a] == 0]
        # if not roots:
        #     #* There has to be ≥1 root in a DAG.
        #     return False
        
        visited = set()
        def dfs(node, path):
            if node in path:
                #* Detect back-edges (cycles)
                return 
            
            if node in visited:
                #! This node has already been fully processed and proven to be safe (cycle-free), so we can skip it.
                return True
            
            visited.add(node)
            path.add(node)
            for child in adjlist[node]:
                if not dfs(child, path):
                    #* Detected a cycle.
                    return False
            path.remove(node)
            return True
        
        for node in range(numCourses):
            if node in visited: 
                continue
            if not dfs(node, set()):
                return False            
        return True