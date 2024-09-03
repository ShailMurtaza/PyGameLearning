import pygame
import numpy as np
from clip import cohen_sutherland_clip
from colors import COLORS

WIDTH, HEIGHT = 500, 500
run = True
clock = pygame.time.Clock()
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

near = 1e-5
far = 20

# Points for CUBE
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


f = 1 # Focal Length
def main():
    angle = 0
    while run:
        new_points = rotate_y(POINTS, angle) # Rotate every point by 1 degree after every iteration
        new_points = translate(new_points, 0, 0, 4) # Translated on z-axis to make object smaller and fit in frustum

        new_points = projection(new_points, f)
        # clipped_vertices = []
        # for i in EDGES:
        #     P1 = new_points[i[0]]
        #     P2 = new_points[i[1]]
        #     COLOR = i[2]
        #     result = cohen_sutherland_clip(P1, P2)
        #     if result != None:
        #         clipped_vertices.append((result[0], result[1], COLOR))
        # new_points = clipped_vertices


        # Draw EDGES of CUBE
        for i in new_points:
            P1 = perspective_divide(i[0])
            P2 = perspective_divide(i[1])
            P1 = map_to_screen(P1[0], P1[1])
            P2 = map_to_screen(P2[0], P2[1])
            COLOR = i[2]
            # Draw line from P1 to P2 with '2PX' width
            pygame.draw.line(WIN, COLOR, P1, P2, 2)

        # Draw Edges of Cube without clipping
        # for i in EDGES:
        #     P1 = perspective_divide(new_points[i[0]])
        #     P2 = perspective_divide(new_points[i[1]])

        #     COLOR = i[2]
        #     # if (P1[0] < 0 or P1[1] < 0 or P1[0] > 1 or P1[1] > 1 or P2[0] < 0 or P2[1] < 0 or P2[0] > 1 or P2[1] > 1):
        #     #     continue
        #     P1 = map_to_screen(P1[0], P1[1])
        #     P2 = map_to_screen(P2[0], P2[1])
        #     pygame.draw.line(WIN, COLOR, P1, P2, 2)

        angle += 1
        draw_win()
        events()

        clock.tick(60) # FPS


# Draw Window
def draw_win():
    pygame.display.update()
    WIN.fill((0, 0, 0))


# Handle Events
def events():
    global run
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False


def projection(vertices, f):
    ar = WIDTH/HEIGHT
    projection_matrix = np.array([
        [f / (ar), 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, -(far + near)/(far-near), 1],
        [0, 0, -2*far*near/(far-near), 0]
    ])
    return vertices @ projection_matrix


# Get 3D vertex and return 2D perpective projection
def perspective_divide(vertex):
    x, y, z, w = vertex
    x2d = (f * x / w)
    y2d = f * y / w
    return x2d, y2d


# Linear interpolation
# x-axis [-1, 1] to [0, WIDTH]
# y-axis [1, -1] to [0, HEIGHT]
def map_to_screen(x, y):
    screen_x = (x + 1) / 2 * WIDTH
    screen_y = (1 - y) / 2 * HEIGHT
    return (screen_x, screen_y)


def rotate_y(vertices, angle):
    angle = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(angle), 0, np.sin(angle), 0],
        [0, 1, 0, 0],
        [-np.sin(angle), 0, np.cos(angle), 0],
        [0, 0, 0, 1]
    ])
    return vertices @ rotation_matrix


def translate(vertices, tx, ty, tz):
    translation_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [tx, ty, tz, 1]
    ])
    return vertices @ translation_matrix


main()
