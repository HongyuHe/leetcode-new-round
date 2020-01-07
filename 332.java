// don't fully understand why adding to the front will do the job whilst backtracking doesn't work;

import java.util.*;

class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        // build adjList
        Map<String, PriorityQueue<String>> adjList = new HashMap<String, PriorityQueue<String>>();
        for (List<String> ticket : tickets) {
            String src = ticket.get(0);
            String dst = ticket.get(1);

            adjList.putIfAbsent(src, new PriorityQueue<String>((s1, s2) -> s1.compareTo(s2)));
            adjList.get(src).add(dst);
        }

        LinkedList<String> itinerary = new LinkedList<String>();
        Queue<String> children = adjList.getOrDefault("JFK", null);
        if (children == null)
            return new ArrayList<>();

        while (!children.isEmpty()) { // can be disconnected -> No
            String child = children.poll();
            dfsReconstruct(child, itinerary, adjList);
        }
        itinerary.addFirst("JFK");

        return itinerary;
    }

    void dfsReconstruct(String parent, LinkedList<String> itinerary, Map<String, PriorityQueue<String>> adjList) {

        Queue<String> children = adjList.getOrDefault(parent, null);

        while (children != null && !children.isEmpty()) {
            String child = children.poll();
            dfsReconstruct(child, itinerary, adjList);
        }
    }
}

// Below is backtracking method: Time Limit Exceeded!

class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        // build adjList
        Map<String, LinkedList<String>> adjList = new HashMap<String, LinkedList<String>>();
        // Set<String> airports = new HashSet<String>();

        for (List<String> ticket : tickets) {
            String src = ticket.get(0);
            String dst = ticket.get(1);

            // airports.add(src);
            // airports.add(dst);
            adjList.putIfAbsent(src, new LinkedList<String>());
            adjList.get(src).add(dst);
        }

        for (List<String> children : adjList.values()) {
            children.sort((s1, s2) -> s1.compareTo(s2));
        }
        // System.out.println(adjList);

        List<String> itinerary = new ArrayList<String>();
        List<String> children = adjList.getOrDefault("JFK", null);
        if (children == null)
            return new ArrayList<>();

        itinerary.add("JFK");
        String prevChild = null;
        while (!adjList.values().stream().allMatch(chdr -> chdr.isEmpty())) {

            if (prevChild != null) {
                itinerary.remove(prevChild); // backtracking;
                children.add(prevChild); // add to tail;
            }

            String currChild = children.remove(0); // poll from the front
            itinerary.add(currChild);

            // System.out.println("Children: "+children);

            dfsReconstruct(currChild, itinerary, adjList);
            prevChild = currChild;
        }

        // System.out.println(adjList);
        // System.out.println(itinerary);

        return itinerary;
    }

    void dfsReconstruct(String parent, List<String> itinerary, Map<String, LinkedList<String>> adjList) {

        // System.out.println("Try: "+parent);

        List<String> children = adjList.getOrDefault(parent, null);
        if (children == null)
            return;

        String prevChild = null;
        while (!adjList.values().stream().allMatch(chdr -> chdr.isEmpty())) {

            if (prevChild != null) {
                itinerary.remove(prevChild); // backtracking;
                children.add(prevChild); // add to tail;
            }

            String currChild = children.remove(0); // poll from the front
            itinerary.add(currChild);
            dfsReconstruct(currChild, itinerary, adjList);
            prevChild = currChild;
        }
    }
}

/*
 * 
 * Take away: 1. using priority queue;
 * 
 * 1. directed graph; 2. has cycles --> lexical tie breaker;
 * ["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"] [a, b]
 * [a, c] [b, c] [c, a] [c, b]
 * 
 * To-do: 1. construct adjList using proority queue; 2. each time pop out an
 * optimal edge; 3. dfs until children == null;
 * 
 * 
 */
