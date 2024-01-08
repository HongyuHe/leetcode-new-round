class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int):
        from collections import defaultdict
        import heapq as hq
        """
        Dijkstra shortest path
        """
        #* Distances to the src
        distances = defaultdict(lambda: float('inf'))
        adjlist = defaultdict(list)
        #* Build adjacency list
        for s, d, w in flights:
          #* Use weight w as the sorting key
          adjlist[s].append( (w, s, d, 0) )
        #* Base case
        distances[src] = 0
        visited = set([src])
        minheap = adjlist[src].copy()
        hq.heapify(minheap)

        while minheap:
          w, s, d, radius = hq.heappop(minheap)
          print(f"Popped {(w, s, d, radius)}")
          if d in visited or radius > k:
            continue
          visited.add(d)
          print(f"Visited {d=}")
          #* Update the distance to d
          distances[d] = min(w, distances[d])
          if d == dst:
            return distances[d]

          #* Include all its neighbors
          for w, s, d, _ in adjlist[d]:
            #! Push the distance to the src, not the distance to the neighbor!
            distance = w + distances[s]
            hq.heappush(minheap, (distance, s, d, radius+1) )
            print(f"Pushed {(distance, s, d, radius+1)}")

        return -1
