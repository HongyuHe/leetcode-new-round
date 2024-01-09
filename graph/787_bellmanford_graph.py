class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Shortest path + k-hop contraint
        -> Bellman ford
        """
        distances = [float('inf')] * n
        #* Base case
        distances[src] = 0
        #* BFS
        while k >= 0:
          new_distances = distances.copy()
          #* TODO: Use adjacency list instead
          for s, d, w in flights:
            #! Checking and updating the NEW distance with the OLD distance.
            new_distances[d] = min(new_distances[d], distances[s]+w)
          distances = new_distances
          k -= 1
        return distances[dst] if distances[dst] < float('inf') else -1

