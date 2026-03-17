class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Plan: Use Khan's topological sort algorithm
            * Build the graph as an adj list
                * Record the indegrees of each node (how many courses depend on it)
            * BFS with queues containing free course that have 0 dependencies.
            * When the queue is empty, check if we've finished all courses.
        """
        from collections import defaultdict, deque

        adjlist = defaultdict(list)
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            adjlist[b].append(a)
            indegrees[a] += 1
        
        roots = [n for n in range(numCourses) if indegrees[n] == 0]
        if not roots:
            #* DAG has ≥1 root.
            return False
        
        queue = deque(roots)
        num_taken = 0
        while queue:
            node = queue.popleft()
            # node = queue.pop()
            #? Doesn't matter it's a queue or stack?
            '''
            for Kahn’s algorithm, using a stack or a queue both works.
            The reason is that the algorithm only requires this invariant:
                At each step, pick any node whose current indegree is 0.
            '''
            num_taken += 1

            for child in adjlist[node]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append(child)
        
        return num_taken == numCourses

        