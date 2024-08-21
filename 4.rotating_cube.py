import pygame
import math

WIDTH, HEIGHT = 800, 600
run = True
clock = pygame.time.Clock()

class COLORS:
    red = (255, 30, 70)
    green = (11, 218, 81)
    blue = (31, 81, 255)
    orange = (255, 172, 28)
    white = (255, 255, 255)

# Points for CUBE
POINTS = [
    [-1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0],
    [1.0, -1.0, 1.0],
    [-1.0, -1.0, 1.0],

    [-1.0, 1.0, -1.0],
    [1.0, 1.0, -1.0],
    [1.0, -1.0, -1.0],
    [-1.0, -1.0, -1.0],
]

EDGES = (
    (0, 1), (1, 2), (2, 3), (3, 0), # Square 1
    (4, 5), (5, 6), (6, 7), (7, 4), # Square 2
    (0, 4), (1, 5), (2, 6), (3, 7), # Join both Squares
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


def vertices_2d(vertices, f):
    vertices_2d_list = []
    for i in vertices:
        vertices_2d_list.append(projection(i, f))
    return vertices_2d_list


def draw_points(vertices, color):
        for v in vertices:
            pygame.draw.circle(WIN, color, v, 2)


def draw_lines(points, color):
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i+1) % len(points)]
        pygame.draw.line(WIN, color, p1, p2)


# Get 3D vertices and return 2D perpective projection
def projection(vertex, f):
    x, y, z = vertex
    x2d = f * x / z
    y2d = f * y / z
    return map_to_screen(x2d, y2d)


# Linear interpolation
# x-axis [-1, 1] to [0, WIDTH]
# y-axis [1, -1] to [0, HEIGHT]
def map_to_screen(x, y):
    screen_x = (x + 1) / 2 * WIDTH
    screen_y = (1 - y) / 2 * HEIGHT
    return (screen_x, screen_y)


def rotate_y(vertex, angle):
    x, y, z = vertex
    new_x = x * math.cos(angle) + z * math.sin(angle)
    new_z = -x * math.sin(angle) + z * math.cos(angle)
    return [new_x, y, new_z]


def rotate_points(points, angle):
    angle = math.radians(angle)
    shape_rotated = []
    for i in points:
        point_rot = rotate_y(i, angle)
        shape_rotated.append(point_rot)
    return shape_rotated

def translate_z(points, offset_z):
    translated_points = []
    for x, y, z in points:
        translated_points.append([x, y, z + offset_z])
    return translated_points


f = 0.9 # Focal Length
def main():
    global POINTS
    while run:
        translated_points = translate_z(POINTS, 4)

        # Convert all 3D POINTS to 2D
        v2d = vertices_2d(translated_points, f)

        draw_points(v2d, COLORS.red)

        # Draw EDGES of CUBE
        for i in EDGES:
            pygame.draw.line(WIN, COLORS.white, v2d[i[0]], v2d[i[1]])
        POINTS = rotate_points(POINTS, -1) # Rotate every point by 1 degree after every iteration

        draw_win()
        events()

        clock.tick(25) # FPS


main()
