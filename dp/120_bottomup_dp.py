class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # * It's similar to a (special) binary tree.
        # * Can't do greedy due to the adjacency restriction, 
        # * i.e., suboptimal for now, but better in the long run.
        num_layers = len(triangle)
        # * Base case: leaves to be 0's.
        cache = triangle[-1].copy()

        # * Start from the 2nd last layer.
        for i in range(num_layers-2, -1, -1):
            layer = triangle[i]
            for j in range(len(layer)):
                node = layer[j]
                path_sum_min = node + min(cache[j], cache[j+1])
                # * Update the cache.
                cache[j] = path_sum_min
        return cache[0]

