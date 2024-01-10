class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int):
        from collections import defaultdict
        import heapq as hq
        """
        Dijkstra shortest path
        """
        #* Distances to the src
        adjlist = defaultdict(list)
        #* Build adjacency list
        for s, d, w in flights:
          #* Use weight w as the sorting key
          adjlist[s].append( (w, d) )
          
        minhops = [float('inf')] * n
        minheap = [(0, 0, src)]
        hq.heapify(minheap)

        while minheap:
          dist, d, h = hq.heappop(minheap)
          if h > minhops[d]:
            #! Allow the same node to be visited multiple times if it can be reached with fewer hops
            #* We can do this because we are using the min heap, 
            #* which guarantees that the first time we reach a node, it is the shortest path to that node.
            continue
          else:
            minhops[d] = h
          
          if d == dst:
            #* Return immediately once we reach the destination, since it's the shortest path
            #* Otherwise, we will continue to explore other paths due to the min hops condition, which will be longer
            return dist

          h += 1
          if h > k+1:
            #* Don't consider paths that are more than k+1 hops away
            continue
          #* Include all its neighbors
          for weight, nxt in adjlist[d]:
            #! Push the distance to the src, not the distance to the next node!
            distance = weight + dist
            hq.heappush(minheap, (distance, nxt, h) )

        return -1
