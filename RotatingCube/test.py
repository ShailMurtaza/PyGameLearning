import numpy as np

WIDTH, HEIGHT = 800, 800
near = 1
far = 10

# Constants for outcodes
LEFT   = 0b000001  # x < -w
RIGHT  = 0b000010  # x > +w
BOTTOM = 0b000100  # y < -w
TOP    = 0b001000  # y > +w
NEAR   = 0b010000  # z < -w
FAR    = 0b100000  # z > +w

def compute_outcode(x, y, z, w):
    print(x, y, z, w)
    outcode = 0
    if x < -w:
        outcode |= LEFT
        print(f"Left Out")
    if x > w:
        outcode |= RIGHT
        print(f"Right Out")
    if y < -w:
        outcode |= BOTTOM
        print(f"Bottom Out")
    if y > w:
        outcode |= TOP
        print(f"Top Out")
    if z < 0:
        outcode |= NEAR
        print(f"Near Out")
    if z > w:
        outcode |= FAR
        print(f"Far Out")
    if outcode == 0:
        print("Point is inside")
    return outcode


def projection(vertices):
    ar = WIDTH/HEIGHT
    f = 1/np.tan(np.radians(90/2))
    projection_matrix = np.array([
        [f / ar, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, far/(far - near), 1],
        [0, 0, -far*near/(far-near), 0]
    ])
    return vertices @ projection_matrix


a = np.array([0.506, -1., -0.820, 1.])
# a = np.array([0.9, -0.9, 0, 1.])
print(f"a = {a}")
b = projection(a)
print(f"b = {b}")
compute_outcode(b[0], b[1], b[2], b[3])
