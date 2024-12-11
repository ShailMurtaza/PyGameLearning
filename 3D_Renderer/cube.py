import numpy as np
from colors import COLORS

POINTS = np.array([
    [-1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, -1.0, 1.0, 1.0],
    [-1.0, -1.0, 1.0, 1.0],
    [-1.0, 1.0, -1.0, 1.0],
    [1.0, 1.0, -1.0, 1.0],
    [1.0, -1.0, -1.0, 1.0],
    [-1.0, -1.0, -1.0, 1.0],
])


EDGES = (
    (0, 1, COLORS.teal), (1, 2, COLORS.green), (2, 3, COLORS.magenta), (3, 0, COLORS.red), # Square 1
    (4, 5, COLORS.cyan), (5, 6, COLORS.blue), (6, 7, COLORS.pink), (7, 4, COLORS.yellow), # Square 2
    (0, 4, COLORS.indigo), (1, 5, COLORS.purple), (2, 6, COLORS.orange), (3, 7, COLORS.white), # Join both Squares
)


