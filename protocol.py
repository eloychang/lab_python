
from classes.distance_matrix import distance_matrix
from classes.solution import solution

class protocol:
    
    def __init__(self, filename):
        
        self._load_shipments(filename)
        
        
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
