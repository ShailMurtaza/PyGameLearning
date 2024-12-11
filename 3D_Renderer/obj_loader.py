import numpy as np
import re

def parse_obj_to_numpy(filename):
    points = []
    edges = set()
    
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('v '):  # Vertex line
                # Extract vertex coordinates
                parts = line.split()
                vertex = [float(coord) for coord in parts[1:]]
                vertex.append(1.0)
                points.append(vertex)
            elif line.startswith('f '):  # Face line
                # Extract face indices
                parts = line.split()
                face_indices = [int(part.split('/')[0]) - 1 for part in parts[1:]]
                # Add edges based on face indices
                for i in range(len(face_indices)):
                    edge = (face_indices[i], face_indices[(i + 1) % len(face_indices)])
                    if edge[0] > edge[1]:
                        edge = (edge[1], edge[0])
                    edges.add(edge)
    
    # Convert lists to numpy arrays
    points = np.array(points)
    edges = np.array(list(edges))
    
    return points, edges

if __name__ == "__main__":
    # Usage
    filename = 'cube.obj'
    points, edges = parse_obj_to_numpy(filename)
    print("Points:", points)
    print("Edges:", edges)
    # input()