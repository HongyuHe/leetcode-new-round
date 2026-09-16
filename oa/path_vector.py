#!/usr/bin/env python3
"""
Path Vector Routing Simulator
Run this file directly to test your implementation.
"""
import time

class Node:
    def __init__(self, name: str):
        self.name = name
        # routing_table maps destination -> (cost, path)
        self.routing_table = {self.name: (0, [self.name])}
        self.neighbors = {} # maps neighbor_name -> link_cost

    def add_neighbor(self, neighbor_name: str, cost: int):
        self.neighbors[neighbor_name] = cost
        self.routing_table[neighbor_name] = (cost, [self.name, neighbor_name])

    def receive_update(self, neighbor_name: str, neighbor_table: dict) -> bool:
        """
        Processes a routing table update from a neighbor.
        
        Args:
            neighbor_name (str): The name of the neighbor sending the update.
            neighbor_table (dict): The neighbor's routing table {destination: (cost, path)}
        
        Returns:
            bool: True if this node's routing table was changed, False otherwise.
        """
        table_changed = False
        link_cost = self.neighbors[neighbor_name]

        # ==========================================
        # TODO: Implement Path Vector update logic
        # 1. Iterate through destinations in neighbor_table.
        # 2. Check for routing loops (is self.name already in the neighbor's path?).
        # 3. Calculate the new cost (link_cost + neighbor's cost).
        # 4. If the destination is unknown, OR the new cost is strictly better 
        #    than the current cost, update self.routing_table and set table_changed = True.
        # ==========================================
        for dest, (cost, path) in neighbor_table.items():
            if self.name in path:
                continue
            new_cost = link_cost + cost
            if dest not in self.routing_table or new_cost < self.routing_table[dest][0]:
                #* Found a lower-cost path
                self.routing_table[dest] = (new_cost, [self.name] + path)
                table_changed = True
        
        return table_changed

# ==========================================
# SIMULATION & TEST FRAMEWORK (Do not modify)
# ==========================================
def simulate_network(nodes_dict: dict) -> int:
    """Runs the distributed path vector algorithm until convergence."""
    converged = False
    iterations = 0
    max_iterations = 1000 # Increased to allow stress tests to finish
    
    while not converged:
        converged = True
        iterations += 1
        
        # Snapshot current tables to simulate simultaneous exchange
        tables_snapshot = {name: dict(node.routing_table) for name, node in nodes_dict.items()}
        
        for name, node in nodes_dict.items():
            for neighbor_name in node.neighbors:
                neighbor_table = tables_snapshot[neighbor_name]
                if node.receive_update(neighbor_name, neighbor_table):
                    converged = False
                    
        # Failsafe for infinite loops (e.g., if loop prevention is broken)
        if iterations > max_iterations:
            raise RuntimeError(f"Simulation did not converge after {max_iterations} iterations. Check loop prevention!")
            
    return iterations

def run_tests():
    print("--- Running Path Vector Routing Tests ---")
    tests_passed = 0
    total_tests = 4
    
    # Test 1: Standard Network
    try:
        nodes1 = {name: Node(name) for name in ['A', 'B', 'C']}
        nodes1['A'].add_neighbor('B', 2); nodes1['A'].add_neighbor('C', 5)
        nodes1['B'].add_neighbor('A', 2); nodes1['B'].add_neighbor('C', 1)
        nodes1['C'].add_neighbor('A', 5); nodes1['C'].add_neighbor('B', 1)
        
        iters = simulate_network(nodes1)
        table_a = nodes1['A'].routing_table
        
        assert 'C' in table_a, "Node A did not learn a route to C"
        assert table_a['C'][0] == 3, f"Expected cost 3, got {table_a['C'][0]}"
        assert table_a['C'][1] == ['A', 'B', 'C'], f"Expected path ['A', 'B', 'C'], got {table_a['C'][1]}"
        print(f"✅ Test 1 Passed: Standard Network (Converged in {iters} iterations)")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 1 Failed: {e}")

    # Test 2: Edge Case - Disconnected Subnets
    try:
        nodes2 = {name: Node(name) for name in ['A', 'B', 'X', 'Y']}
        nodes2['A'].add_neighbor('B', 1); nodes2['B'].add_neighbor('A', 1)
        nodes2['X'].add_neighbor('Y', 1); nodes2['Y'].add_neighbor('X', 1)
        
        simulate_network(nodes2)
        assert 'X' not in nodes2['A'].routing_table, "Node A should not know about Node X"
        print("✅ Test 2 Passed: Disconnected Subnets")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 2 Failed: {e}")

    # Test 3: Stress Test - 50-Node Ring Topology
    # Verifies loop prevention doesn't falsely block legitimate long paths
    try:
        start_time = time.time()
        ring_size = 50
        nodes3 = {str(i): Node(str(i)) for i in range(ring_size)}
        for i in range(ring_size):
            next_node = str((i + 1) % ring_size)
            prev_node = str((i - 1) % ring_size)
            nodes3[str(i)].add_neighbor(next_node, 1)
            nodes3[str(i)].add_neighbor(prev_node, 1)
            
        iters = simulate_network(nodes3)
        exec_time = time.time() - start_time
        
        # In a 50 node ring, the furthest node from '0' is '25', with distance 25
        cost_to_25, path_to_25 = nodes3['0'].routing_table['25']
        
        assert cost_to_25 == 25, f"Expected cost 25 to opposite side of ring, got {cost_to_25}"
        assert len(path_to_25) == 26, f"Expected path length 26 (including source), got {len(path_to_25)}"
        print(f"✅ Test 3 Passed: 50-Node Ring Topology (Converged in {iters} iters, took {exec_time:.4f}s)")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 3 Failed: {e}")

    # Test 4: Stress Test - Dense Complete Graph (15 Nodes)
    # Generates a massive amount of updates; tests efficiency of convergence
    try:
        start_time = time.time()
        dense_size = 15
        nodes4 = {str(i): Node(str(i)) for i in range(dense_size)}
        for i in range(dense_size):
            for j in range(dense_size):
                if i != j:
                    nodes4[str(i)].add_neighbor(str(j), 10) # direct cost is 10
        
        # Create one ultra-cheap indirect path 0 -> 1 -> 2 ... -> 14
        for i in range(dense_size - 1):
            nodes4[str(i)].neighbors[str(i+1)] = 1
            nodes4[str(i+1)].neighbors[str(i)] = 1
            
        iters = simulate_network(nodes4)
        exec_time = time.time() - start_time
        
        cost_to_last, path = nodes4['0'].routing_table[str(dense_size - 1)]
        assert cost_to_last == 10, f"Expected direct path cost 10 to win over long indirect path cost 14, got {cost_to_last}"
        assert len(path) == 2, f"Expected direct path length 2, got {len(path)}"
        
        print(f"✅ Test 4 Passed: 15-Node Dense Graph (Converged in {iters} iters, took {exec_time:.4f}s)")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 4 Failed: {e}")

    print(f"\nResults: {tests_passed}/{total_tests} Tests Passed")

if __name__ == "__main__":
    run_tests()
    