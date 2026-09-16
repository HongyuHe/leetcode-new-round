#!/usr/bin/env python3
"""
Link State Routing Simulator
Run this file directly to test your implementation.
"""
import time

def compute_link_state(graph: dict, source: str) -> tuple[dict, dict]:
    """
    Computes the shortest path from the source to all other nodes using Dijkstra's Algorithm.
    
    Args:
        graph (dict): A dictionary of dictionaries representing the network adjacency.
                      Example: {'A': {'B': 2, 'C': 5}, 'B': {'A': 2, 'C': 1}}
        source (str): The starting node.

    Returns:
        tuple (distances, paths):
            - distances: A dict mapping each node to its shortest distance from the source.
            - paths: A dict mapping each node to the shortest path (list of nodes) from the source.
                     (For unreachable nodes, the path should remain an empty list [])
    """
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    paths = {node: [] for node in graph}
    paths[source] = [source]
    
    # ==========================================
    # TODO: Implement Dijkstra's Algorithm here
    # ==========================================
    import heapq as hq
    
    minqueue = [(0, source)]
    while minqueue:
        shortest_path, closest_node = hq.heappop(minqueue)
        
        if shortest_path > distances[closest_node]:
            #* Guard against stale link states (see below).
            continue
        
        neighbors = graph[closest_node]
        for neighbor, edge_weight in neighbors.items():
            new_dist = shortest_path + edge_weight
            #* Check if we've found a shorter path
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                paths[neighbor] = paths[closest_node] + [neighbor]
                #* Push the update into the heap
                #! The stale copy is still in the queue, that's why we need the above guard.
                hq.heappush(minqueue, (new_dist, neighbor))
    
    return distances, paths

# ==========================================
# TEST FRAMEWORK (Do not modify)
# ==========================================
import time

def run_tests():
    print("--- Running Link State Routing Tests ---")
    tests_passed = 0
    total_tests = 6
    
    # Test 1: Simple Triangle (Unique shortest path)
    try:
        graph1 = {'A': {'B': 2, 'C': 5}, 'B': {'A': 2, 'C': 1}, 'C': {'A': 5, 'B': 1}}
        d1, p1 = compute_link_state(graph1, 'A')
        assert d1['C'] == 3, f"Expected distance 3, got {d1.get('C')}"
        assert p1['C'] == ['A', 'B', 'C'], f"Expected path ['A', 'B', 'C'], got {p1.get('C')}"
        print("✅ Test 1 Passed: Simple Triangle")
        tests_passed += 1
    except AssertionError as e:
        print(f"❌ Test 1 Failed: {e}")

    # Test 2: Complex Network
    try:
        graph2 = {
            'U': {'V': 2, 'W': 5, 'X': 1}, 'V': {'U': 2, 'W': 3, 'Y': 2},
            'W': {'U': 5, 'V': 3, 'Y': 1, 'Z': 5}, 'X': {'U': 1, 'Y': 1},
            'Y': {'V': 2, 'W': 1, 'X': 1, 'Z': 2}, 'Z': {'W': 5, 'Y': 2}
        }
        d2, p2 = compute_link_state(graph2, 'U')
        assert d2['Z'] == 4, f"Expected distance to Z to be 4, got {d2.get('Z')}"
        assert p2['Z'] == ['U', 'X', 'Y', 'Z'], f"Expected path to Z to be ['U', 'X', 'Y', 'Z'], got {p2.get('Z')}"
        print("✅ Test 2 Passed: Complex Network")
        tests_passed += 1
    except AssertionError as e:
        print(f"❌ Test 2 Failed: {e}")

    # Test 3: Edge Case - Disconnected Graph
    try:
        graph3 = {'A': {'B': 1}, 'B': {'A': 1}, 'C': {'D': 1}, 'D': {'C': 1}}
        d3, p3 = compute_link_state(graph3, 'A')
        assert d3['C'] == float('inf'), f"Expected distance to C to be inf, got {d3.get('C')}"
        assert p3['C'] == [], f"Expected path to C to be [], got {p3.get('C')}"
        print("✅ Test 3 Passed: Disconnected Graph")
        tests_passed += 1
    except AssertionError as e:
        print(f"❌ Test 3 Failed: {e}")

    # Test 4: Edge Case - Single Node Graph
    try:
        graph4 = {'Solo': {}}
        d4, p4 = compute_link_state(graph4, 'Solo')
        assert d4['Solo'] == 0, f"Expected distance 0, got {d4.get('Solo')}"
        assert p4['Solo'] == ['Solo'], f"Expected path ['Solo'], got {p4.get('Solo')}"
        print("✅ Test 4 Passed: Single Node Graph")
        tests_passed += 1
    except AssertionError as e:
        print(f"❌ Test 4 Failed: {e}")

    # Test 5: Stress Test - Large Linear Graph (1000 nodes)
    try:
        start_time = time.time()
        graph5 = {str(i): {} for i in range(1000)}
        for i in range(1000):
            if i > 0: graph5[str(i)][str(i-1)] = 1
            if i < 999: graph5[str(i)][str(i+1)] = 1
            
        d5, p5 = compute_link_state(graph5, '0')
        exec_time = time.time() - start_time
        
        assert d5['999'] == 999, f"Expected distance 999, got {d5.get('999')}"
        print(f"✅ Test 5 Passed: 1000-Node Linear Graph (took {exec_time:.4f}s)")
        tests_passed += 1
    except AssertionError as e:
        print(f"❌ Test 5 Failed: {e}")

    # Test 6: THE STALE QUEUE BOMB
    # This topology forces Dijkstra to find thousands of progressively better 
    # paths to the same nodes, flooding the Priority Queue with stale entries.
    try:
        start_time = time.time()
        N = 500
        graph6 = {str(i): {} for i in range(N)}
        
        for i in range(N):
            for j in range(i + 1, N):
                # The direct path is expensive, but adjacent nodes are very cheap.
                # This tricks the algorithm into queueing terrible paths early on, 
                # only to incrementally find better ones as it crawls along the graph.
                weight = 1 if j == i + 1 else 1000 * (j - i)
                graph6[str(i)][str(j)] = weight
                graph6[str(j)][str(i)] = weight
                
        d6, p6 = compute_link_state(graph6, '0')
        exec_time = time.time() - start_time
        
        # Verify correctness
        assert d6[str(N-1)] == N-1, f"Expected cost {N-1}, got {d6.get(str(N-1))}"
        
        print(f"✅ Test 6 Passed: 500-Node Stale Queue Bomb (took {exec_time:.4f}s)")
        
        if exec_time > 0.5:
            print("   🐌 WARNING: Your code is slow! It likely evaluated the neighbors of over 120,000 stale entries.")
            print("   👉 Add this line at the top of your while loop: if current_dist > distances[current_node]: continue")
        else:
            print("   ⚡ SPEED RUN: Your optimization guard successfully bypassed the stale entries!")
            
        tests_passed += 1
    except AssertionError as e:
        print(f"❌ Test 6 Failed: {e}")

    print(f"\nResults: {tests_passed}/{total_tests} Tests Passed")

if __name__ == "__main__":
    run_tests()