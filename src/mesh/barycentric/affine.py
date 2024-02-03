import numpy as np 
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve

class Affine:
    def __init__(self):
        self.vertices = []
        self.parameter_points = {}
    
    def add_spring(self, i, j, Dij):
        pass
    
    def setup_linear_systems(self):
        pass

    def solve_for_interior_vertices(self, A, U_bar, V_bar):
        pass 

affine = Affine()

