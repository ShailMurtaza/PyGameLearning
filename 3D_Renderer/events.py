import pygame

class Key:
    def __init__(self, key, ):
        self.pressed = False
        self.key = key


# If key is pressed or not
KEYS = {
    "W": (Key(pygame.K_w), "y", 1),
    "A": (Key(pygame.K_a), "x", -1),
    "S": (Key(pygame.K_s), "y", -1),
    "D": (Key(pygame.K_d), "x", 1),
    "Q": (Key(pygame.K_q), "z", 1),
    "E": (Key(pygame.K_e), "z", -1),

    "I": (Key(pygame.K_i), "rotate_x", 4),
    "K": (Key(pygame.K_k), "rotate_x", -4),
    "L": (Key(pygame.K_l), "rotate_y", 4),
    "J": (Key(pygame.K_j), "rotate_y", -4),
    "U": (Key(pygame.K_u), "rotate_z", 4),
    "O": (Key(pygame.K_o), "rotate_z", -4),
}


# Transformations
TRANSFORMATION = {
    "rotate_x": 0.0,
    "rotate_y": 0.0,
    "rotate_z": 0.0,
    "x": 0.0,
    "y": 0.0,
    "z": 0.0
}


# Handle Events
def events(dt):
    run = True
    transformation_factor = 5
    
    for _, (key, axis, direction) in KEYS.items():
        if key.pressed:
            TRANSFORMATION[axis] += direction * transformation_factor * dt
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            for _, (key, axis, direction) in KEYS.items():
                if (e.key == key.key):
                    key.pressed = True

        elif e.type == pygame.KEYUP:
            for _, (key, axis, direction) in KEYS.items():
                if (e.key == key.key):
                    key.pressed = False
        
        elif e.type == pygame.MOUSEWHEEL:
            if e.y == 1:
                TRANSFORMATION["z"] += 0.1
            else:
                TRANSFORMATION["z"] -= 0.1
    return run
