import java.io.*;
import java.util.*;

// Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

// For example, in this diagram, 6 and 8 have a common ancestor of 4.

//          14  13
//          |   |
// 1   2    4   12
//  \ /   / | \ /
//   3   5  8  9
//    \ / \     \
//     6   7     11

// parentChildPairs1 = [
//     (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
//     (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
// ]

// Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.

// Sample input and output:

// hasCommonAncestor(parentChildPairs1, 3, 8) => false
// hasCommonAncestor(parentChildPairs1, 5, 8) => true
// hasCommonAncestor(parentChildPairs1, 6, 8) => true
// hasCommonAncestor(parentChildPairs1, 6, 9) => true
// hasCommonAncestor(parentChildPairs1, 1, 3) => false
// hasCommonAncestor(parentChildPairs1, 7, 11) => true
// hasCommonAncestor(parentChildPairs1, 6, 5) => true
// hasCommonAncestor(parentChildPairs1, 5, 6) => true

// Additional example: In this diagram, 4 and 12 have a common ancestor of 11.

//         11
//        /  \
//       10   12
//      /  \
// 1   2    5
//  \ /    / \
//   3    6   7
//    \        \
//     4        8

// parentChildPairs2 = [
//     (11, 10), (11, 12), (10, 2), (10, 5), (1, 3),
//     (2, 3), (3, 4), (5, 6), (5, 7), (7, 8),
// ]

// hasCommonAncestor(parentChildPairs2, 4, 12) => true
// hasCommonAncestor(parentChildPairs2, 1, 6) => false
// hasCommonAncestor(parentChildPairs2, 1, 12) => false

// n: number of pairs in the input

public class Solution {
    public static void main(String[] argv) {

        // int[][] parentChildPairs = new int[][] {
        // {1, 3}, {2, 3}, {3, 6}, {5, 6}, {5, 7},
        // {4, 5}, {4, 8}, {4, 9}, {9, 11}
        // };
        // // int[][] parentChildPairs = new int[][] {
        // // {1, 3}
        // // };

        // System.out.println(findNodesWithZeroAndOneParents(parentChildPairs));

        int[][] parentChildPairs1 = new int[][] { { 1, 3 }, { 2, 3 }, { 3, 6 }, { 5, 6 }, { 5, 7 }, { 4, 5 }, { 4, 8 },
                { 4, 9 }, { 9, 11 }, { 14, 4 }, { 13, 12 }, { 12, 9 } };

        int[][] parentChildPairs2 = new int[][] { { 11, 10 }, { 11, 12 }, { 10, 2 }, { 10, 5 }, { 1, 3 }, { 2, 3 },
                { 3, 4 }, { 5, 6 }, { 5, 7 }, { 7, 8 } };

        // System.out.println(hasCommonAncestor(parentChildPairs1, 4, 12));
        System.out.println(hasCommonAncestor(parentChildPairs1, 3, 8));
        System.out.println(hasCommonAncestor(parentChildPairs1, 5, 8));
        System.out.println(hasCommonAncestor(parentChildPairs1, 6, 8));
        System.out.println(hasCommonAncestor(parentChildPairs1, 6, 9));
        System.out.println(hasCommonAncestor(parentChildPairs1, 1, 3));
        System.out.println(hasCommonAncestor(parentChildPairs1, 7, 11));
        System.out.println(hasCommonAncestor(parentChildPairs1, 6, 5));
        System.out.println(hasCommonAncestor(parentChildPairs1, 5, 6));

    }

    static boolean hasCommonAncestor(int[][] parentChildPairs, int node1, int node2) {

        Map<Integer, ArrayList<Integer>> adjList = new HashMap<Integer, ArrayList<Integer>>();
        Map<Integer, HashSet<Integer>> colors = new HashMap<Integer, HashSet<Integer>>();

        Set<Integer> nodes = new LinkedHashSet<Integer>();
        for (int[] edge : parentChildPairs) {
            nodes.add(edge[0]);
            nodes.add(edge[1]);
            adjList.putIfAbsent(edge[0], new ArrayList<Integer>());
            adjList.get(edge[0]).add(edge[1]);
        }
        // System.out.println(adjList);

        for (Map.Entry<Integer, ArrayList<Integer>> entry : adjList.entrySet()) {
            int root = entry.getKey();

            dfsColoring(root, root, colors, adjList);
            colors.putIfAbsent(root, new HashSet<Integer>());
            colors.get(root).add(root);
            // System.out.println(entry.getValue());
        }

        // Set<Integer> commonColors = colors.get(node1)
        // .stream()
        // .anyMatch( cls -> (colors.get(node2)));

        for (int color1 : colors.get(node1)) {
            if (colors.get(node2).contains(color1))
                return true;
        }

        return false;
    }

    static void dfsColoring(int root, int color, Map<Integer, HashSet<Integer>> colors,
            Map<Integer, ArrayList<Integer>> adjList) {
        // base case
        Set<Integer> cL = colors.getOrDefault(root, null);
        if (cL != null) {
            if (cL.contains(color))
                return;
        }

        List<Integer> children = adjList.getOrDefault(root, null);
        if (children == null)
            return;

        for (int child : children) {
            cL = colors.putIfAbsent(child, new HashSet<Integer>());
            colors.get(child).add(color);
            dfsColoring(child, color, colors, adjList);
        }
        // System.out.println(colors);
    }

    static List<ArrayList<Integer>> findNodesWithZeroAndOneParents(int[][] parentChildPairs) {
        List<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>(2);
        res.add(new ArrayList<Integer>());
        res.add(new ArrayList<Integer>());

        if (parentChildPairs.length == 0) {
            return res;
        }

        Map<Integer, ArrayList<Integer>> adjList = new HashMap<Integer, ArrayList<Integer>>();

        Set<Integer> nodes = new LinkedHashSet<Integer>();
        for (int[] edge : parentChildPairs) {
            nodes.add(edge[0]);
            nodes.add(edge[1]);
            adjList.putIfAbsent(edge[1], new ArrayList<Integer>());
            adjList.get(edge[1]).add(edge[0]);
        }
        // System.out.println(nodes);

        for (int node : nodes) {
            List<Integer> children = adjList.getOrDefault(node, null);

            if (children == null) {
                res.get(0).add(node);
            } else if (children.size() == 1) {
                res.get(1).add(node);
            }

        }
        // System.out.println(res); Space: O(n^2) Time: O(n)

        return res;
    }
}
