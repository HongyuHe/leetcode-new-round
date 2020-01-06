/*
    Cycle detection:

    1. undirected gragh
    2. x==y: x <--> y
    3. x!=y: x -\\- y
        x==x x==y
    
    to-dos:
        1. build graph from equal-equations using adjacency list;
        2. check satisfaction asscording to !=;

*/

import java.util.*;

class Solution {
    public boolean equationsPossible(String[] equations) {
        Set<String> conditions = new LinkedHashSet<String>(); // HashSet next in O(h/n)
        Map<Character, ArrayList<Character>> adjList = new HashMap<Character, ArrayList<Character>>();
        // build adjacency list

        for (String equation : equations) {
            char rNode = equation.charAt(0);
            char lNode = equation.charAt(3);
            char sign = equation.charAt(1);

            if (sign == '=') {
                adjList.putIfAbsent(rNode, new ArrayList<Character>());
                adjList.get(rNode).add(lNode);
                if (rNode != lNode) {
                    adjList.putIfAbsent(lNode, new ArrayList<Character>());
                    adjList.get(lNode).add(rNode);
                }

            } else {
                if (!conditions.contains(rNode + "" + lNode) && !conditions.contains(lNode + "" + rNode))
                    conditions.add(rNode + "" + lNode); // "xy"
            }
        }

        // System.out.println(adjList);
        // System.out.println(conditions);

        // check reachability dfs
        Set<Character> visited = new HashSet<Character>();
        for (String condition : conditions) {
            char root = condition.charAt(0);
            char target = condition.charAt(1);

            if (dfsFind(root, target, adjList, visited)) {
                return false;
            }
            visited.clear();
        }
        return true;
    }

    Boolean dfsFind(char parent, char target, Map<Character, ArrayList<Character>> adjList, Set<Character> visited) {
        if (parent == target)
            return true;

        ArrayList<Character> children = adjList.get(parent);
        if (children == null)
            return false;
        visited.add(parent);

        for (char child : children) {
            if (!visited.contains(child) && dfsFind(child, target, adjList, visited)) {
                return true;
            }
        }

        return false;
    }
}
