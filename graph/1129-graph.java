/*
    take away: 
     1. using bfs with cyclic graph could lead to the need of setting limit of level; 
     2. using JVM string pool to build set, saving memory by eliminating duplication;

    constrains:
    1. single-source shortest path to every node;
    2. colors are alternate in along the path;
    3. dijkstra-like: priority queue + check colour --> lowest cost+diff colour
    4. uniformed edge cost of 1
    5. loop is permitted but we should limit the level of the search tree; maximum
    
*/

import java.util.*;

class Solution {
    public int[] shortestAlternatingPaths(int n, int[][] red_edges, int[][] blue_edges) {

        // build the adjacency list: [parent] -> {[child, colour]. [] ...} (red:-1,
        // blue: 1)
        Map<Integer, ArrayList<int[]>> adjList = new HashMap<Integer, ArrayList<int[]>>();

        for (int[] edge : red_edges) {
            adjList.putIfAbsent(edge[0], new ArrayList<int[]>());
            adjList.get(edge[0]).add(new int[] { edge[1], -1 });
        }
        for (int[] edge : blue_edges) {
            adjList.putIfAbsent(edge[0], new ArrayList<int[]>());
            adjList.get(edge[0]).add(new int[] { edge[1], +1 });
        }

        // dijkstra (bfs)
        int[] distances = new int[n];
        Arrays.fill(distances, -1);
        distances[0] = 0;

        Deque<int[]> deque = new ArrayDeque<int[]>();
        ArrayList<int[]> firstLevel = adjList.getOrDefault(0, null);
        if (firstLevel == null)
            return distances;
        deque.addAll(firstLevel);

        int level = 0;
        int maxLevel = red_edges.length + blue_edges.length; // limit the level of the search tree;
        Set<String> visited = new HashSet<>();

        while (!deque.isEmpty() && level <= maxLevel) {
            level++;
            int size = deque.size();

            while (size-- > 0) {
                int[] parent = deque.poll();
                int parentNode = parent[0];
                int colour = parent[1];

                visited.add(parentNode + "" + colour);

                // record its distance
                if (distances[parentNode] == -1)
                    distances[parentNode] = level;

                // check the colour of the edge and add;
                ArrayList<int[]> children = adjList.getOrDefault(parentNode, null);
                if (children == null)
                    continue;

                for (int[] child : children) {
                    if (child[1] == -colour && !visited.contains(child[0] + "" + child[1]))
                        deque.add(child);
                }
            }
        }
        return distances;

    }
}
