import pygame

WIDTH, HEIGHT = 800, 600
run = True
clock = pygame.time.Clock()
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

# TBRL
inside = 0
top = 0b1000
bottom = 0b0100
right = 0b0010
left = 0b0001


def calc_outcode(x, y):
    code = inside
    if x < x_min:
        code |= left
    elif x > x_max+x_min:
        code |= right

    if y < y_min:
        code |= top
    elif y > y_max+y_min:
        code |= bottom

    return code


def clip_draw(x1, y1, x2, y2):
    code1 = calc_outcode(x1, y1)
    code2 = calc_outcode(x2, y2)
    accept = False

    while True:
        # if code1 & code2 is 0000 then both points are inside of frustum. Don't do anything they will be drawn
        if code1 | code2 == 0:
            accept = True
            break
        # if code1 & code2 is not 0000 then both points are outside of frustum
        elif code1 & code2:
            break
        else:
            outcode = code1 if code1 != 0 else code2
            x = 0
            y = 0

            if outcode & top:
                x = (y_min - y1) * (x2-x1) / (y2-y1) + x1
                y = y_min
            elif outcode & bottom:
                x = (y_max + y_min - y1) * (x2-x1) / (y2-y1) + x1
                y = y_max + y_min
            elif outcode & right:
                x = x_max + x_min
                y = (x_max + x_min - x1) * (y2 - y1) / (x2 - x1) + y1
            elif outcode & left:
                x = x_min
                y = (x_min - x1) * (y2 - y1) / (x2 - x1) + y1

            if outcode == code1:
                x1 = x
                y1 = y
                code1 = calc_outcode(x1, y1)
            else:
                x2 = x
                y2 = y
                code2 = calc_outcode(x2, y2)
    if accept:
        pygame.draw.line(WIN, "#ffffff", (x1, y1), (x2, y2))


x_min = 150
x_max = 350
y_min = 300
y_max = 200

x1 = 160
y1 = 400
x2 = 460
y2 = 600


def main():
    while run:
        pygame.draw.rect(WIN, "#fffff0", pygame.Rect(x_min, y_min, x_max, y_max), 2)
        pygame.draw.line(WIN, "#ff0000", (x1, y1), (x2, y2))
        clip_draw(x1, y1, x2, y2)

        draw_win()
        events()
        clock.tick(60) # FPS

main()
