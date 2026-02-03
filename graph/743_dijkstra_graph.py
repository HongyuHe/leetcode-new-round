class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int):
      """
      Shortest path without constraints -> Dijkstra
      • Disconnected graph, return -1
      """
      from collections import defaultdict
      import heapq as hq

      distances = [float('inf')] * (n+1)
      distances[0] = 0 #* Unused
      #* Base case
      distances[k] = 0

      adjlist = defaultdict(list)
      for s, d, w in times:
        #* Put weight first as the sort key
        adjlist[s].append( (w, d) )
      
      minheap = adjlist[k].copy()
      hq.heapify(minheap)
      #* Prevent cycles
      visited = set([k])
      while minheap:
        #* The `t` here is the time from `k` (NOT from the source of the edge) to `d`
        t, d = hq.heappop(minheap)
        if d in visited:
          continue
        else:
          visited.add(d)
        distances[d] = min(distances[d], t)
        #* Add outgoing edges
        for w, dst in adjlist[d]:
          #! Record the distance from `k` (NOT from the source of the edge) to the `dst`. 
          time = w + distances[d]
          hq.heappush(minheap, (time, dst))

      time_max = max(distances)
      return time_max if time_max < float('inf') else -1