class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """
        Example: [A B B C C C], n = 2
            * A B C _ B C _ _ C
            * C A B C _ B C
            * C B A 
            -> Prioritize most frequent tasks first
        
        Plan:
            * Work queue tracking which task is ready (ready ts, count)
            * Max heap prioritizing more frequent tasks
        """
        from collections import Counter, deque
        import heapq as hq

        timer = 0
        counts = Counter(tasks)
        maxheap = [-count for count in counts.values()]
        hq.heapify(maxheap)
        taskq = deque()

        while maxheap or taskq:
            if maxheap:
                count = hq.heappop(maxheap)
            
                count += 1
                timer += 1
                if count < 0:
                    taskq.append((timer+n, count))
                
            while taskq:
                ts, count = taskq.popleft()
                if ts == timer:
                    hq.heappush(maxheap, count)
                elif not maxheap:
                    # No work in the heap, fast forward to the next task 
                    timer = ts
                    hq.heappush(maxheap, count)
                else:
                    # Have work in the heap to do, put the task back
                    taskq.appendleft((ts, count))
                    break
        
        return timer 
