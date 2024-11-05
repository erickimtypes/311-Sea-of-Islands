# Import the functions from each task file
from task1_leader_circulation import dijkstra_leader_circulation
from task2_resource_allocation import distribute_resource
from task3_distribute_resources import Island, Canoe, distribute_resources
import random
import time

class Route:
    def __init__(self, destination, travel_time):
        self.destination = destination
        self.travel_time = travel_time

class Graph:
    def __init__(self, num_islands):
        self.islands = [f"Island_{i}" for i in range(num_islands)]
        self.routes = {island: [] for island in self.islands}

    def add_route(self, start, end, travel_time):
        self.routes[start].append(Route(end, travel_time))

def test_task1():
    print("\n--- Testing Task 1: Leader Circulation ---")
    graph = {
        'Hawaii': [('Tahiti', 10), ('Aotearoa', 25)],
        'Tahiti': [('Hawaii', 10), ('Rapanui', 20)],
        'Aotearoa': [('Hawaii', 25)],
        'Rapanui': [('Tahiti', 20)]
    }
    populations = {
        'Hawaii': 200,
        'Tahiti': 150,
        'Aotearoa': 100,
        'Rapanui': 50
    }
    start_island = 'Hawaii'
    dijkstra_leader_circulation(graph, start_island, populations)
    """
    Expected output: 
    --- Testing Task 1: Leader Circulation ---
    Leader visits Hawaii with travel time 0
    Leader visits Tahiti with travel time 10
    Leader visits Aotearoa with travel time 25
    Leader visits Rapanui with travel time 30
    """
    
if __name__ == "__main__":
    print("Running all task tests:")
    test_task1()
    

# Function for testing task2_resource_allocation, function "distribute_resource"

def test_task2(num_islands, num_routes, capacity):

    print("\n--- Testing Task 2: Resource Allocation ---")
    # Initialize a random graph with a specified number of islands and routes
    graph = Graph(num_islands)
    for _ in range(num_routes):
        start = random.choice(graph.islands)
        end = random.choice(graph.islands)
        travel_time = random.randint(1, 20)
        if start != end:  # Avoid self-loops
            graph.add_route(start, end, travel_time)
    
    # Set up the initial conditions
    start_island = graph.islands[0]
    initial_quantity = 1000  # Example initial quantity of resources
    resource = "Test Resource"  # Example resource
    
    # Measure the time to execute the distribution
    distances = distribute_resource(graph, start_island, resource, initial_quantity, capacity)
    
    # Output the time taken and a summary of distances
    print(f"Distribution completed for {num_islands} islands and {num_routes} routes.")
    print("Sample distances:", {k: distances[k] for k in list(distances)[:10]})  # Show distances for a sample of islands

# Run the test function with different scales of islands and routes
test_task2(num_islands=100, num_routes=500, capacity=50)
test_task2(num_islands=500, num_routes=2000, capacity=50)
test_task2(num_islands=1000, num_routes=5000, capacity=50)

# Function for testing task3_distribute_resources
def test_task3():

    print("\n--- Testing Task 3: Full Coverage With Limited Canoes ---")
    # Define islands and travel times (graph representation)
    travel_times = {
        "South America": [("Rapa Nui", 2), ("Tahiti", 4)],
        "Rapa Nui": [("New Zealand", 1), ("Hawaii", 3)],
        "Tahiti": [("Hawaii", 2)],
        "New Zealand": [],
        "Hawaii": []
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

    # Expected distribution: each reachable island should receive at least one unit
    expected_distribution = {
        "South America": 3,  # Origin
        "Rapa Nui": 1,
        "Tahiti": 1,
        "New Zealand": 1,
        "Hawaii": 1
    }

    # Check if the actual distribution matches the expected results
    all_tests_passed = True
    for island, expected_count in expected_distribution.items():
        actual_count = resources_distributed.get(island, 0)
        if actual_count != expected_count:
            all_tests_passed = False
            print(f"Test failed for {island}: expected {expected_count}, got {actual_count}")
    
    if all_tests_passed:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")

# Run the test function
if __name__ == "__main__":
    test_task3()
