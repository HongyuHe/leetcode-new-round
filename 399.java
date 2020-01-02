// This is one of the most ugly code I have ever written...

/*
 * 'a' -2-> 'b' -3-> 'c' 'e'/'x' -1 (reverse: 1/weight)
 * 
 * HashMap<String, Array<Object[2]>> HashMap['a'] = { ('b', 2) } HashMap['b'] =
 * { ('a', -2), ('c', 3) ...}
 * 
 * 1. look up the map find dst (bfs) 2. multiply all the weights 3. if there is
 * no path --> -1
 */

class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {

        // build the adjency list
        Map<String, ArrayList<Object[]>> adjList = new HashMap<String, ArrayList<Object[]>>();

        for (int i = 0; i < equations.size(); i++) {
            double dist = values[i];
            String srcNode = equations.get(i).get(0);
            String dstNode = equations.get(i).get(1);

            ArrayList<Object[]> adj = adjList.putIfAbsent(srcNode, new ArrayList<Object[]>());
            if (adj == null) {
                adjList.get(srcNode).add(new Object[] { dstNode, dist });
            } else {
                adj.add(new Object[] { dstNode, dist });
            }

            if (srcNode != dstNode) {
                adj = adjList.putIfAbsent(dstNode, new ArrayList<Object[]>());
                if (adj == null) {
                    adjList.get(dstNode).add(new Object[] { srcNode, 1 / dist });
                } else {
                    adj.add(new Object[] { srcNode, 1 / dist });
                }
            }
        }

        // solve queries
        double[] answers = new double[queries.size()];
        int i = 0;
        for (List<String> query : queries) {
            double ans = solver(query, adjList);
            answers[i] = ans;
            i++;
        }

        return answers;

    }

    double solver(List<String> query, Map<String, ArrayList<Object[]>> adjList) {

        String src = query.get(0);
        String dest = query.get(1);

        ArrayList<Object[]> parentAdj = adjList.getOrDefault(src, null);
        if (src.equals(dest) && parentAdj != null)
            return 1;
        if (!adjList.keySet().contains(dest))
            return -1;

        if (parentAdj != null) {
            // dfs
            for (Object[] child : parentAdj) {

                double ans = dfs(dest, child, 1, adjList, new HashSet<String>(Arrays.asList(src)));

                if (ans != -1.0)
                    return ans;
            }
        }
        return -1.0;
    }

    double dfs(String dest, Object[] root, double weightSoFar, Map<String, ArrayList<Object[]>> adjList,
            HashSet<String> visited) {

        String rootNode = (String) root[0];
        double weight = (double) root[1];

        if (!dest.equals(rootNode)) {
            visited.add(rootNode); // visited

            ArrayList<Object[]> rootAdj = new ArrayList<Object[]>(adjList.get(rootNode)); // make a copy!
            rootAdj.removeIf(node -> visited.contains((String) node[0]));

            if (rootAdj.isEmpty()) {
                return -1; // no successor
            } else {
                for (Object[] child : rootAdj) {
                    double ans = dfs(dest, child, weightSoFar * weight, adjList, visited);

                    if (ans != -1.0)
                        return ans;
                }
                return -1;
            }

        }
        return weightSoFar * weight; // find dest
    }

}
