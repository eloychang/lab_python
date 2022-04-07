
from classes.distance_matrix import distance_matrix
from classes.solution import solution

import random

random.seed(0)

class protocol:
    
    def __init__(self, filename, routes):
        
        self._load_shipments(filename)
        
        self._d_matrix = distance_matrix(self._shipments)
        
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
        self._solution = None
        for i in range(iterations):
            
            solution = self._local_search()
            
            if self._solution is None or solution.cost() < self._solution.cost():
                self._solution = solution
                
    def _local_search(self):
        solution = self._generate_solution()
        ready = False
        while not ready:        
            neighborhood = solution.generate_neighborhood() 
            best_solution = {
                "cost" : solution.cost(),
                "neighbord" : None
            } 
            for route1 in range(self._total_routes):
                
                solution.remove_neighbord(route1, neighborhood[route1], self._d_matrix)
                
                for route2 in range(self._total_routes):
                    
                    if route1 == route2:
                        continue
                        
                    solution.add_neighbord(route2, neighborhood[route1], self._d_matrix)
                    
                    if solution.cost() < best_solution["cost"]:
                        best_solution["cost"] = solution.cost()
                        best_solution["neighbord"] = (route1, route2)
                        
                    solution.remove_neighbord(route2, neighborhood[route1], self._d_matrix)
                    
            solution.add_neighbord(route1, neighborhood[route1], self._d_matrix)
                    
            ready = best_solution["neighbord"] is None
            
            if not ready:
                solution.remove_neighbord(best_solution["neighbord"][0], self._d_matrix)
                solution.add_neighbord(best_solution["neighbord"][1], neighborhood[best_solution["neighbord"][0]], self._d_matrix)
                
        return solution
    
    def _generate_solution(self):
        
        total_shipments_by_route = len(self._shipments) // self._total_routes       
        shipments_left = len(self._shipments) - (total_shipments_by_route * self._total_routes)
        
        shipments = set([x["id"] for x in self._shipments])
        shipments_by_route = []
        for route in range(self._total_routes):
            add_left = 1 if shipments_left > 0 else 0
            shipments_by_route.append(random.sample(shipments, total_shipments_by_route + add_left))
            shipments = shipments - set(shipments_by_route[route])
            shipments_left -= 1
            
        return solution(shipments_by_route, self._d_matrix)
                    
    def show_best_solution(self):        
        print(f"Total distance: {round(self._solution.cost(),2)}")
        for route in self._solution:
            print(f"* Route_{route.id}:")
            print(f"\t- Total shipments: {route.total_shipments()}")
            print(f"\t- Total distance: {round(route.cost(),2)}")
            
