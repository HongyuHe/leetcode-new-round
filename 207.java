// Cycle detection: DFS backtracking

import java.util.*;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (numCourses == 1 || prerequisites.length == 0) {
            return true;
        }

        HashMap<Integer, ArrayList<Integer>> adjList = new HashMap<Integer, ArrayList<Integer>>();

        for (int[] pair : prerequisites) {
            adjList.putIfAbsent(pair[0], new ArrayList<Integer>());
            adjList.get(pair[0]).add(pair[1]);
        }

        Set<Integer> visited = new HashSet<Integer>();

        for (int i = 0; i < numCourses; i++) {
            if (!dfsChecker(i, adjList, visited))
                return false;
        }
        return true;
    }

    Boolean dfsChecker(int node, HashMap<Integer, ArrayList<Integer>> adjList, Set<Integer> visited) {

        if (visited.contains(node))
            return false;

        visited.add(node);

        ArrayList<Integer> adjNodes = adjList.getOrDefault(node, null);
        if (adjNodes != null) {
            for (int adj : adjNodes) {
                if (!dfsChecker(adj, adjList, visited))
                    return false;
            }
        }

        visited.remove(node); // backtracking
        return true;
    }
}

/*
 * 1 <- 0 <- 1
 * 
 * 5 [1,2][3,4][4,3]: 1<-2<-3<-1
 * 
 * 
 * 1. build adjecency list 2. dfs -> cycle detection
 * 
 */