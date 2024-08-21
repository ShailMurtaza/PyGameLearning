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

shape1 = [
    [-1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0],
    [1.0, -1.0, 1.0],
    [-1.0, -1.0, 1.0],

    [-1.0, 1.0, 2.0],
    [1.0, 1.0, 2.0],
    [1.0, -1.0, 2.0],
    [-1.0, -1.0, 2.0],
]


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

f = 0.3
sign = 0.02
def main():
    global run, f, sign
    while run:
        v2d = vertices_2d(shape1, f)
        draw_points(v2d, COLORS.red)
        draw_lines(v2d, COLORS.white)

        draw_win()
        events()
        input()
        run = False

main()
