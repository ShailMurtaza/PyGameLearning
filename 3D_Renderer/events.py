import pygame

# If key is pressed or not
KEYS = {
    "W": False,
    "A": False,
    "S": False,
    "D": False,
}


# Transformations
TRANSFORMATION = {
    "angle": 0.0,
    "x": 0.0,
    "y": 0.0,
    "z": 0.0
}


# Handle Events
def events(dt):
    run = True
    transformation_factor = 5
    if (KEYS["A"]):
        TRANSFORMATION["x"] -= transformation_factor * dt
    if (KEYS["D"]):
        TRANSFORMATION["x"] += transformation_factor * dt
    if (KEYS["W"]):
        TRANSFORMATION["y"] += transformation_factor * dt
    if (KEYS["S"]):
        TRANSFORMATION["y"] -= transformation_factor * dt
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:
                KEYS["A"] = True
            elif e.key == pygame.K_d:
                KEYS["D"] = True
            elif e.key == pygame.K_w:
                KEYS["W"] = True
            elif e.key == pygame.K_s:
                KEYS["S"] = True
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_a:
                KEYS["A"] = False
            elif e.key == pygame.K_d:
                KEYS["D"] = False
            elif e.key == pygame.K_w:
                KEYS["W"] = False
            elif e.key == pygame.K_s:
                KEYS["S"] = False
        
        elif e.type == pygame.MOUSEWHEEL:
            if e.y == 1:
                TRANSFORMATION["z"] += 0.1
            else:
                TRANSFORMATION["z"] -= 0.1
    return run
