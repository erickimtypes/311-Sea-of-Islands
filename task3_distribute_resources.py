from collections import deque, defaultdict

# Initialize the graph
class Island:
    def __init__(self, name):
        self.name = name
        self.resources_received = 0

# Initialize the canoe
class Canoe:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_capacity = capacity

    def load(self):
        """Reload the canoe to full capacity at the origin."""
        self.current_capacity = self.capacity

# Function to distribute resources to islands
def distribute_resource(origin, islands, travel_times, canoe):
    # Dictionary to keep track of resources received by each island
    resources_distributed = defaultdict(int)
    queue = deque([(origin, 0)])  # Queue holds tuples of (current island, distance from origin)

    while queue:
        current_island, current_distance = queue.popleft()

        # Try to load the canoe with resources at the origin
        if current_island == origin:
            canoe.load()

        # Distribute resources at the current island if the canoe has enough capacity
        if canoe.current_capacity > 0:
            resources_distributed[current_island] += 1
            canoe.current_capacity -= 1
            print(f"Delivered to {current_island}. Remaining capacity: {canoe.current_capacity}")

        # Enqueue neighboring islands for distribution if there is capacity remaining
        for neighbor, travel_time in travel_times[current_island]:
            if resources_distributed[neighbor] == 0:  # Only add neighbors not yet reached
                queue.append((neighbor, current_distance + travel_time))

        # If the canoe is out of capacity, return it to the origin for reloading
        if canoe.current_capacity == 0 and current_island != origin:
            queue.append((origin, 0))  # Return to origin for reloading
            print("Returning canoe to origin for reloading.")

    return resources_distributed

# Test Case
# Define islands and travel times (graph representation)
travel_times = {
    "South America": [("Rapa Nui", 2)],
    "Rapa Nui": [("Tahiti", 1), ("Hawaii", 3)],
    "Tahiti": [("New Zealand", 2), ("Samoa", 1)],
    "Hawaii": [("Samoa", 2)],
    "New Zealand": [],
    "Samoa": []
}

# Instantiate islands and a canoe with limited capacity
islands = {name: Island(name) for name in travel_times}
canoe = Canoe(capacity=3)

# Distribute resources starting from origin 'A'
origin = "South America"
resources_distributed = distribute_resource(origin, islands, travel_times, canoe)

# Display results
print("\nResource distribution summary:")
for island, count in resources_distributed.items():
    print(f"{island} received {count} units of the resource.")