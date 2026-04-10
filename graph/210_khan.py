class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """ 15min!
        Plan
            * Build the depency graph as an adj list
            * Id the roots
                * If no roots -> []
            * Use Khan's algorithm, starting from the free courses having 0 indegrees
            * Build the course list as we pop out free coruses from the list.
        """
        from collections import defaultdict, deque
        adjlist = defaultdict(list)
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            adjlist[b].append(a)
            indegrees[a] += 1
        
        roots = [n for n in range(numCourses) if indegrees[n] == 0]
        if not roots: 
            #* Not a DAG
            return []
        
        queue = deque(roots)
        curriculum = []
        while queue:
            course = queue.popleft()
            curriculum.append(course)
            for child in adjlist[course]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append(child)
        
        return curriculum if len(curriculum) == numCourses else []
