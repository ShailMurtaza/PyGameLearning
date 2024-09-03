import pygame
from time import sleep

WIDTH, HEIGHT = 800, 600
run = True

class COLORS:
    red = (255, 30, 70)
    green = (11, 218, 81)
    blue = (31, 81, 255)
    orange = (255, 172, 28)
    white = (255, 255, 255)

POINTS = [
    [-1.0, 1.0, 4.0],
    [1.0, 1.0, 4.0],
    [1.0, -1.0, 4.0],
    [-1.0, -1.0, 4.0],

    [-1.0, 1.0, 2.0],
    [1.0, 1.0, 2.0],
    [1.0, -1.0, 2.0],
    [-1.0, -1.0, 2.0],
]

EDGES = (
    (0, 1, COLORS.white), (1, 2, COLORS.white), (2, 3, COLORS.white), (3, 0, COLORS.white), # Square 1
    (4, 5, COLORS.white), (5, 6, COLORS.white), (6, 7, COLORS.white), (7, 4, COLORS.white), # Square 2
    (0, 4, COLORS.white), (1, 5, COLORS.white), (2, 6, COLORS.white), (3, 7, COLORS.white), # Join both Squares
)



pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_win():
    pygame.display.update()
    WIN.fill((0, 0, 0))

def events():
    global run
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False


# Get 3D vertices and return 2D perpective projection
def vertices_2d(vertices, d):
    vertices_2d_list = []
    for i in vertices:
        vertices_2d_list.append(projection(i, d))
    return vertices_2d_list


def draw_points(vertices, color):
        for v in vertices:
            pygame.draw.circle(WIN, color, v, 4)

def draw_lines(points, color):
    pairs = []
    for i in points:
        for x in points:
            if i != x:
                pairs.append((i, x))
    for i in pairs:
        p1, p2 = i
        pygame.draw.line(WIN, color, p1, p2)

def projection(vertex, f):
    x2d = f * vertex[0] / vertex[2]
    y2d = f * vertex[1] / vertex[2]
    return map_to_screen(x2d, y2d)

def map_to_screen(x, y):
    screen_x = int((x + 1) / 2 * WIDTH)
    screen_y = int((1 - y) / 2 * HEIGHT)
    return (screen_x, screen_y)

f = 1
def main():
    global run, f
    while run:
        v2d = vertices_2d(POINTS, f)

        draw_points(v2d, COLORS.red)

        # Draw EDGES of CUBE
        for i in EDGES:
            pygame.draw.line(WIN, i[2], v2d[i[0]], v2d[i[1]], 2)

        draw_win()
        events()

main()
