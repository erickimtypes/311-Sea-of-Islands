# Import the functions from each task file
from task1_leader_circulation import dijkstra_leader_circulation

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
