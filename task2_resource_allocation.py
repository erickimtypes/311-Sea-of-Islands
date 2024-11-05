import heapq

def distribute_resource(graph, start_island, resource, initial_quantity, capacity):
    # Initialize distances to infinity
    distances = {island: float('inf') for island in graph.islands}
    distances[start_island] = 0
    
    # Create the priority queue (min-heap) 
    pq = [(0, start_island, initial_quantity)]
    
    # Loop while there are islands to visit
    while pq:
        # Dequeue island with shortest travel time
        travel_time, current_island, available_quantity = heapq.heappop(pq)
        
        # If we are out of cargo, skip further distribution from this island
        if available_quantity <= 0:
            continue

        # Process each neighboring route
        for route in graph.routes[current_island]:
            next_island = route.destination
            next_travel_time = travel_time + route.travel_time
            
            # Check if we found a shorter path to the neighboring island
            if next_travel_time < distances[next_island]:
                distances[next_island] = next_travel_time
                
                # Calculate the cargo to take based on remaining capacity
                cargo_to_distribute = min(available_quantity, capacity)
                
                # Update priority queue with next island and remaining cargo
                heapq.heappush(pq, (next_travel_time, next_island, available_quantity - cargo_to_distribute))
    
    # Returns minimum travel times to all reachable islands
    return distances
