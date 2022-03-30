
class route:
    
    def __init__(self, idx, shipments, dists):
        self.id = idx
        self._shipments = {}
        self._worst_shipment = (None, 0)
        self._cost = 0
        for shipment in shipments:
            self._shipments[shipment] = 0
            for s in shipments:
                if shipment == s:
                    continue
                self._shipments[shipment] += dists.get_dist(shipment, s)
            self._cost += self._shipments[shipment]
            if self._shipments[shipment] > self._worst_shipment[1]:
                self._worst_shipment = (shipment, self._shipments[shipment])
        
        self._base_shipments = self._shipments.copy()
        self._base_worst_shipment = self._worst_shipment
        
    def cost(self):
        return self._cost
                
    def drop_shipment(self, droped_shipment, dists):
        self._worst_shipment = (None, 0)
        self._shipments.pop(droped_shipment)
        for shipment in self._shipments.keys():
            self._shipments[shipment] -= dist.get_dist(shipment, droped_shipment)
            self._cost -= self._shipments[shipment]
            if self._shipments[shipment] > self._worst_shipment[1]:
                self._worst_shipment = (shipment, self._shipments[shipment])
            
    def add_shipment(self, new_shipment, dist):
        dist_new_shipment = 0
        self._worst_shipment = (None, 0)
        for shipment in self._shipments.keys():
            dist = dist.get_dist(shipment, new_shipment)
            self._shipments[shipment] += dist
            self._cost += self._shipments[shipment]
            if self._shipments[shipment] > self._worst_shipment[1]:
                self._worst_shipment = (shipment, self._shipments[shipment])
                
    def worst_shipment(self):
        return self._worst_shipment[0]
    
    def reset(self):
        self._shipments = self._base_shipments.copy()
        self._worst_shipment = self._base_worst_shipment.copy()
        