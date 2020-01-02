// This is a graph coloring problem

/*
 * int[] colors: 0(unvisited) 1(right set-> default root) -1(left set) using dfs
 * to do graph union where return false if any confliction happened 0 -> 1,3 {0}
 * {1,3}
 */

class Solution {
    public boolean isBipartite(int[][] graph) {
        int[] canvas = new int[graph.length];

        for (int i = 0; i < graph.length; i++) {
            if (canvas[i] == 0 && !dfsPaint(i, 1, canvas, graph)) {
                return false;
            }
        }
        return true;

    }

    Boolean dfsPaint(int root, int color, int[] canvas, int[][] graph) {
        if (canvas[root] != 0)
            return canvas[root] == color;

        canvas[root] = color;

        for (int child : graph[root]) {
            if (!dfsPaint(child, -color, canvas, graph))
                return false;
        }
        return true;
    }
}
// Using set like below would exceed time limit;

/*
 * E1: {}{}
 * 
 * 0 -> 1, 3 ==> {0} {1, 3}
 * 
 * 1 -> 0, 2 ==> [1 | 0, 2] ==> put 1: {1, 3} =search on another set=> put 0:
 * {0} => put 2: {0, 2}
 * 
 * E2: {}{}
 * 
 * use dfs to iteratively add node from the `graph` to find a confliction
 * 
 * 1 -> 0,2 ==> {1}{0,2} 3 -> 0,2 ==> put 3: 1. One of them has 3 -> choose the
 * other set to put 2. None of them has 3 -> check 0, 2 1) Neither of them added
 * yet -> use dfs branching trail -> return 2) find confliction -> return false;
 * 3) one or more campatibaly exist -> add the residuals and choose another set
 * to put node 3;
 * 
 * 0 -> 1,2,3 ==> ...
 * 
 * if all nodes set, -> true otherwise false
 * 
 * 
 */

class Solution {
    public boolean isBipartite(int[][] graph) {

        if (graph.length <= 1)
            return true;

        // no iteration -> ok to use hashset
        Set<Integer> rSet = new HashSet<Integer>();
        Set<Integer> lSet = new HashSet<Integer>();

        // Initialisation
        lSet.add(0);
        for (int child : graph[0]) {
            rSet.add(child);
        }
        // rSet.addAll(Arrays.asList(graph[0]));

        int nextRoot = 1;
        return biCheck(lSet, rSet, nextRoot, graph);
    }

    Boolean biCheck(Set<Integer> lSet, Set<Integer> rSet, int nextRoot, int[][] graph) {

        if (nextRoot >= graph.length) // all nodes are set;
            return true;
        if (graph[nextRoot].length == 0) // empty
            return biCheck(lSet, rSet, nextRoot + 1, graph);

        ArrayList<Integer> children = new ArrayList<>();
        for (int child : graph[nextRoot]) {
            children.add(child);
        }

        // check root
        if (rSet.contains(nextRoot)) {
            // check children in rSet and add children to lSet
            if (children.stream().noneMatch(n -> rSet.contains(n))) {
                lSet.addAll(children);
            } else {
                return false; // confliction
            }

        } else if (lSet.contains(nextRoot)) {
            // check children in lSet and add children to rSet
            if (children.stream().noneMatch(n -> lSet.contains(n))) {
                rSet.addAll(children);
            } else {
                return false; // confliction
            }

        } else { // no root
            // try both sets;
            Set<Integer> r = new HashSet<Integer>(rSet);
            Set<Integer> l = new HashSet<Integer>(lSet);

            l.add(nextRoot); // try add root to left
            if (!biCheck(l, r, nextRoot, 0, graph)) { // failed, backtracking
                Set<Integer> r_ = new HashSet<Integer>(rSet);
                Set<Integer> l_ = new HashSet<Integer>(lSet);
                r_.add(nextRoot); // try add root to right;

                return biCheck(l_, r_, nextRoot, graph); // nextChild = 0
            }
        }
        return biCheck(lSet, rSet, nextRoot + 1, graph);
    }
}