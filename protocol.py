
from classes.distance_matrix import distance_matrix
from classes.solution import solution

class protocol:
    
    def __init__(self, filename, routes):
        
        self._load_shipments(filename)
        
        self._total_routes = routes
        
        
    def _load_shipments(self, filename):
        with open(filename, "r") as file:
            self._shipments = []
            ready = False
            while not ready:
                try:
                    idx, receiver, coordinates = file.readline().split("|")
                    coordinates = [float(x) for x in coordinates.split(",")]
                    self._shipments.append({"id" : int(idx), "receiver" : receiver, "coord" : coordinates})
                except ValueError:
                    ready = True
                    
                    
    def iterative_local_search(self, iterations):
        pass
                    
                    
    def show_best_solution(self):        
        print(f"Total distance: {round(self._solution.cost(),2)}")
        for route in self._solution:
            print(f"* Route_{route.id}:")
            print(f"\t- Total shipments: {route.total_shipments()}")
            print(f"\t- Total distance: {round(route.cost(),2)}")
            
