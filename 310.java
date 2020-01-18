/*
    take away: find and eat tree leaves;

*/

// eat leaves from outside to inside;
class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        // edge cases
        if (n == 1)
            return Collections.singletonList(0);

        if (edges.length == 1) {
            List<Integer> roots = new ArrayList<>();
            roots.add(edges[0][0]);
            roots.add(edges[0][1]);
            return roots;
        }

        Map<Integer, HashSet<Integer>> adjList = new LinkedHashMap<>();
        for (int[] edge : edges) {
            adjList.putIfAbsent(edge[0], new HashSet<>());
            adjList.get(edge[0]).add(edge[1]);
            adjList.putIfAbsent(edge[1], new HashSet<>());
            adjList.get(edge[1]).add(edge[0]);
        }

        Set<Integer> fringe = new LinkedHashSet<Integer>();
        int numNodes = n;
        while (numNodes > 2) {
            for (int node : adjList.keySet()) {
                Set<Integer> children = adjList.get(node);
                if (1 == children.size()) {
                    fringe.add(node);
                }
            }
            numNodes -= fringe.size();
            for (int leave : fringe) {
                Set<Integer> parent = adjList.get(leave);
                adjList.get(parent.toArray()[0]).remove(leave);
                adjList.remove(leave);
            }
            fringe.clear();
        }
        return new ArrayList<Integer>(adjList.keySet());
    }
}

// naive BFS: Timeout
class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        List<Integer> roots = new ArrayList<>();
        // edge cases
        if (n == 1) {
            roots.add(0);
            return roots;
        }
        if (edges.length == 1) {
            roots.add(edges[0][0]);
            roots.add(edges[0][1]);
            return roots;
        }

        Map<Integer, ArrayList<Integer>> adjList = new LinkedHashMap<>();
        for (int[] edge : edges) {
            adjList.putIfAbsent(edge[0], new ArrayList<>());
            adjList.get(edge[0]).add(edge[1]);
            adjList.putIfAbsent(edge[1], new ArrayList<>());
            adjList.get(edge[1]).add(edge[0]);
        }

        Set<Integer> internalNodes = new LinkedHashSet<>();
        for (Map.Entry<Integer, ArrayList<Integer>> entry : adjList.entrySet()) {
            if (entry.getValue().size() > 1) {
                internalNodes.add(entry.getKey());
            }
        }

        if (internalNodes.size() == 1)
            return new ArrayList(internalNodes);

        Queue<int[]> rank = new PriorityQueue<>((r1, r2) -> r1[1] - r2[1]);
        for (int node : internalNodes) {
            int height = findHeight(node, adjList);
            rank.add(new int[] { node, height });
        }

        int minHeight = (rank.isEmpty()) ? -1 : rank.peek()[1];
        while (!rank.isEmpty()) {
            int[] rootInfo = rank.poll();
            if (rootInfo[1] == minHeight)
                roots.add(rootInfo[0]);
        }
        return roots;
    }

    int findHeight(int root, Map<Integer, ArrayList<Integer>> adjList) {
        int height = -1;
        ArrayDeque<Integer> deque = new ArrayDeque<>();
        Set<Integer> visited = new HashSet<Integer>();
        deque.add(root);
        visited.add(root);

        while (!deque.isEmpty()) {
            int len = deque.size();
            height++;

            while (len-- > 0) {
                int parent = deque.pop();
                visited.add(parent);
                List<Integer> children = adjList.get(parent);

                for (int child : children) {
                    if (!visited.contains(child)) {
                        deque.add(child);
                    }
                }
            }
        }
        return height;
    }

}
