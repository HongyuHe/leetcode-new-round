import java.util.*;

/* Topological sorting:

    1. build an adjacency list;
    2. cycle detection;
    3. return the order if doable;
    
    [[2,0],[2,1]] -> 1, 0 <= [2] / 0, 1, 2
    [[0,2],[1,2]] -> 2 <= [1], 0 / 2, 0, 1
*/

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        if (numCourses == 0) {
            return new int[0];
        } else if (numCourses == 1) {
            return new int[1];
        } else if (prerequisites.length == 0) {
            int[] courses = new int[numCourses];
            for (int i = 0; i < numCourses; i++) {
                courses[i] = i;
            }
            return courses;
        }

        // build adjacency list
        Map<Integer, ArrayList<Integer>> adjList = new HashMap<Integer, ArrayList<Integer>>();
        for (int[] pair : prerequisites) {
            adjList.putIfAbsent(pair[0], new ArrayList<Integer>());
            adjList.get(pair[0]).add(pair[1]);
        }
        // System.out.println(adjList);

        Set<Integer> visited = new HashSet<Integer>();
        Set<Integer> order = new LinkedHashSet<Integer>();
        Set<Integer> indep = new LinkedHashSet<Integer>();
        // cycel detection using dfs
        for (int i = 0; i < numCourses; i++) {
            if (checkCycel(i, adjList, prerequisites, order, visited)) {
                // no cycel, add neighbors
                ArrayList<Integer> neighbors = adjList.getOrDefault(i, null);
                if (neighbors != null) {
                    order.add(i);
                } else {
                    indep.add(i);
                }

            } else {
                return new int[0];
            }
        }
        order.addAll(indep);

        int[] out = new int[order.size()];
        int i = 0;
        for (int course : order) {
            out[i] = course;
            i++;
        }

        return out;
    }

    Boolean checkCycel(int node, Map<Integer, ArrayList<Integer>> adjList, int[][] prerequisites, Set<Integer> order,
            Set<Integer> visited) {
        if (visited.contains(node)) {
            return false;
        }

        visited.add(node);
        ArrayList<Integer> neighbors = adjList.getOrDefault(node, null);
        if (neighbors != null) {
            for (int neighbor : neighbors) {
                if (!checkCycel(neighbor, adjList, prerequisites, order, visited))
                    return false;
            }
        }
        visited.remove(node);
        order.add(node); // add node on returning;

        return true;
    }

}
