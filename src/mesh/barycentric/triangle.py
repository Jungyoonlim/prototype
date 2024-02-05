import numpy as np

class TriangleMesh:
    def __init__(self):
        self.vertices = []
        self.triangles = []
        self.edges = []
        self.vertex_map = {}
    
    def load_from_obj(self, filepath):
        with open(filepath, 'r') as file:
            for line in file:
                if line.startswith('v '):
                    _, x, y, z = line.split()
                    self.add_vertex((float(x), float(y), float(z)))
                elif line.startswith('f '):
                    _, v1, v2, v3 = line.split()
                    self.add_triangle(int(v1)-1, int(v2)-1, int(v3)-1)
    
    def calculate_uv_coordinates(self):
        self.uvs = []
        for vtx in self.vertices:
            u = vtx[0]
            v = vtx[1]
            self.uvs.append((u,v))
    
    def display_uv_mapping(self):
        """Display Vertices and their UV Mapping"""
        for i, uv in enumerate(self.uvs):
            print(f"Vertex {i}: UV -> {uv}")


    def add_vertex(self, p):
        self.vertices.append(np.array(p))
        return len(self.vertices) - 1 
    
    def add_triangle(self, p1_idx, p2_idx, p3_idx):
        self.triangles.append([p1_idx, p2_idx, p3_idx])
        self._add_edge(p1_idx, p2_idx)
        self._add_edge(p1_idx, p3_idx)
        self._add_edge(p2_idx, p3_idx)

    def _add_edge(self, p1, p2):
        edge = tuple(sorted([p1, p2]))
        if edge not in self.edges:
            self.edges.append(edge)
    
    def linear_parameterization(self):
        for i, vertex in enumerate(self.vertices):
            u = (vertex[0], vertex[1])
            self.vertex_map[i] = u 

    def display(self):
        """Display vertices and their parameterization."""
        for i, vertex in enumerate(self.vertices):
            print(f"Vertex {i}: {vertex} -> {self.vertex_map.get(i, 'Not mapped')}")

    
mesh = TriangleMesh()
mesh.calculate_uv_coordinates()
mesh.display_uv_mapping()

p1 = mesh.add_vertex((10,0,0))
p2 = mesh.add_vertex((0,1,0))
p3 = mesh.add_vertex((0,0,1))
mesh.add_triangle(p1,p2,p3)

mesh.linear_parameterization()
mesh.display()