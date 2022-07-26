/*
       [ 1,  5,  9],
       [ 3,  7, 13],
       [ 8, 13, 15]

*/

// binary search solution: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/301357/Java-0ms-(added-Python-and-C%2B%2B)%3A-Easy-to-understand-solutions-using-Heap-and-Binary-Search
// my binary tree solution
class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        Queue<int[]> Q = new PriorityQueue<>((n1, n2) -> matrix[n1[0]][n1[1]] - matrix[n2[0]][n2[1]]);
        Q.add(new int[] { 0, 0 });
        Set<String> visited = new HashSet<>();
        visited.add(Integer.toString(0) + "-" + Integer.toString(0));

        int res = -1;
        while (!Q.isEmpty() && k-- > 0) {
            int[] parent = Q.poll();
            int[] childR = new int[2];
            int[] childL = new int[2];
            if (parent[1] + 1 < matrix.length) {
                childR[0] = parent[0];
                childR[1] = parent[1] + 1;
            }
            if (parent[0] + 1 < matrix.length) {
                childL[0] = parent[0] + 1;
                childL[1] = parent[1];
            }
            if (!visited.contains(Integer.toString(childR[0]) + "-" + Integer.toString(childR[1]))) {
                visited.add(Integer.toString(childR[0]) + "-" + Integer.toString(childR[1]));
                Q.add(new int[] { childR[0], childR[1] });
            }
            if (!visited.contains(Integer.toString(childL[0]) + "-" + Integer.toString(childL[1]))) {
                visited.add(Integer.toString(childL[0]) + "-" + Integer.toString(childL[1]));
                Q.add(new int[] { childL[0], childL[1] });
            }
            res = matrix[parent[0]][parent[1]];
        }
        return res;
    }
}