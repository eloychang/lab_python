
from math import sqrt

class distance_matrix:
    
    def __init__(self, data):
        self._dists = {}
        N = len(data)
        for idx_1 in range(N - 1):
            for idx_2 in range(idx_1 + 1, N):
                dist = self._calculate_dist(data[idx_1]["coord"], data[idx_2]["coord"])
                self._dists[(data[idx_1]["id"], data[idx_2]["id"])] = dist
                
        
    def _calculate_dist(self, coord_1, coord_2):
        return sqrt((coord_1[0] - coord_2[0])**2 + (coord_1[1] - coord_2[1])**2)
    
    
    def get_dist(self, idx_1, idx_2):
        if (idx_1, idx_2) in self._dists:
            return self._dists[(idx_1, idx_2)]
        return self._dists[(idx_2, idx_1)]
    