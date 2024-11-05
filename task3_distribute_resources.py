from collections import deque, defaultdict

class Island:
    def __init__(self, name):
        self.name = name
        self.resources_received = 0  # Track resources received

class Canoe:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_load = capacity  # Starts fully loaded

# Distributes resources from an origin island across a directed, weighted graph of islands.
# Each island receives a resource, subject to the canoe's capacity constraints.
# The canoe returns to the origin to reload when empty.
def distribute_resource(origin, islands, travel_times, canoe):
    
    # Queue for BFS, starting from the origin island
    queue = deque([origin])
    visited = set()  # Track visited islands
    visited.add(origin)
    resources_distributed = defaultdict(int)  # Track distributed resources

    while queue:
        current_island = queue.popleft()

        # Check if canoe has enough capacity to distribute to this island
        if canoe.current_load > 0:
            # Distribute a unit of resource
            islands[current_island].resources_received += 1
            resources_distributed[current_island] += 1
            canoe.current_load -= 1  # Decrease load for each distribution

        # If canoe is empty, return to origin to reload
        if canoe.current_load == 0:
            canoe.current_load = canoe.capacity
            queue.append(origin)  # Add origin back to queue to simulate return and reload

        # Add neighbors to queue if they haven't been visited yet
        for neighbor, _ in travel_times.get(current_island, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    # Return the distribution map
    return resources_distributed