import numpy as np

WIDTH, HEIGHT = 800, 800
near = 0.1
far = 100

def projection(vertices):
    f = 1/np.tan(np.radians(90/2)) # Focal Length
    ar = WIDTH/HEIGHT
    projection_matrix = np.array([
        [f / ar, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, far/(far - near), 1],
        [0, 0, -far*near/(far - near), 0]
    ])
    return vertices @ projection_matrix


# Get 3D vertex and return 2D perpective projection
def perspective_divide(vertex):
    x, y, z, w = vertex
    x2d = x / w
    y2d = y / w
    return x2d, y2d


# Linear interpolation
# x-axis [-1, 1] to [0, WIDTH]
# y-axis [1, -1] to [0, HEIGHT]
def map_to_screen(x, y):
    screen_x = (x + 1) / 2 * WIDTH
    screen_y = (1 - y) / 2 * HEIGHT
    return (screen_x, screen_y)

def rotate_x(vertices, angle):
    angle = np.radians(angle)
    rotation_matrix = np.array([
        [1, 0, 0, 0],
        [0, np.cos(angle), np.sin(angle), 0],
        [0, -np.sin(angle), np.cos(angle), 0],
        [0, 0, 0, 1]
    ])
    return vertices @ rotation_matrix

def rotate_y(vertices, angle):
    angle = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(angle), 0, np.sin(angle), 0],
        [0, 1, 0, 0],
        [-np.sin(angle), 0, np.cos(angle), 0],
        [0, 0, 0, 1]
    ])
    return vertices @ rotation_matrix

def rotate_z(vertices, angle):
    angle = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(angle), np.sin(angle), 0, 0],
        [-np.sin(angle), np.cos(angle), 0, 0],
        [0, 0, 1, 0],
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
