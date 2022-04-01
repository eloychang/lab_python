
from classes.route import route

class solution:
    
    def __init__(self, shipments_by_route, dists):
        self._routes = []
        self._cost = 0
        idx = 1
        for shipments in shipments_by_route:
            self._routes.append(route(idx, shipments, dists))
            self._cost +=  self._routes[idx - 1].cost()
            idx += 1        
            
            
    def generate_neighborhood(self):
        neighborhood = []
        for _route in self._routes:
            neighborhood.append((_route.id, _route.worst_shipment()))
        return neighborhood
    
    
    def cost(self):
        return self._cost
    
    
    def __iter__(self):
        for r in self._routes:
            yield r
    
            