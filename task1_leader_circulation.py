import heapq

def dijkstra_leader_circulation(graph, start_island, population):
    # Priority queue for Dijkstra's algorithm
    # Each entry is a tuple (travel_time, -population, island) to prioritize shortest travel time
    # and highest population for islands with equal travel times.
    priority_queue = [(0, -population[start_island], start_island)]
    
    # Dictionary to store the shortest travel time to each island
    shortest_times = {island: float('inf') for island in graph}
    shortest_times[start_island] = 0

    # Visited set to avoid reporting the same island multiple times
    visited = set()
    
    # Run the priority queue until it is empty
    while priority_queue:
        # Pop the island with the shortest travel time (and highest population in case of ties)
        current_time, _, current_island = heapq.heappop(priority_queue)

        if current_island in visited:
            continue
        visited.add(current_island)

        # Simulate knowledge sharing at the current island
        print(f"Leader visits {current_island} with travel time {current_time}")

        # Process all neighbors of the current island
        for neighbor, travel_time in graph[current_island]:
            if neighbor not in visited:
                # Calculate the travel time to reach the neighbor
                new_time = current_time + travel_time

                # If we found a shorter path to the neighbor, update and push to queue
                if new_time < shortest_times[neighbor]:
                    shortest_times[neighbor] = new_time
                    heapq.heappush(priority_queue, (new_time, -population[neighbor], neighbor))

