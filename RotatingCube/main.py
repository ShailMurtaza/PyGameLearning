import pygame
from events import *
from transformations import *
import numpy as np
from clip import cohen_sutherland_clip
from time import time
from obj_loader import parse_obj_to_numpy

clock = pygame.time.Clock()
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


POINTS, EDGES = parse_obj_to_numpy("cube.obj")

cam = (0, 0, 0)

def main():
    run = True
    global TRANSFORMATION
    prev_time = time()
    while run:
        # Calculate delta time for consistent transformations across different Frame Rates
        new_time = time()
        dt = new_time - prev_time
        prev_time = new_time

        new_points = POINTS
        TRANSFORMATION["angle"] += 1
        new_points = rotate_y(new_points, TRANSFORMATION["angle"]) # Rotate every point by 1 degree after every iteration
        new_points = translate(new_points, TRANSFORMATION["x"], TRANSFORMATION["y"], TRANSFORMATION["z"]) # Translated on z-axis to make object smaller and fit in frustum
        new_points = translate(new_points, -cam[0], -cam[1], -cam[2])

        new_points = projection(new_points)

        for i in EDGES:
            P1 = new_points[i[0]]
            P2 = new_points[i[1]]
            COLOR = "#ffffff"
            result = cohen_sutherland_clip(P1, P2)
            if result != None:
                P1 = result[0]
                P2 = result[1]
                draw_point(P1, P2, COLOR)


        draw_win()
        run = events(dt)

        clock.tick(60) # FPS


def draw_point(P1, P2, COLOR):
    P1 = perspective_divide(P1)
    P2 = perspective_divide(P2)
    P1 = map_to_screen(P1[0], P1[1])
    P2 = map_to_screen(P2[0], P2[1])
    # Draw line from P1 to P2 with '1PX' width
    pygame.draw.line(WIN, COLOR, P1, P2, 1)


# Draw Window
def draw_win():
    pygame.display.update()
    WIN.fill((0, 0, 0))


main()
