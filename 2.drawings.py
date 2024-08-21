import pygame

WIDTH, HEIGHT = 800, 600
run = True

class COLORS:
    red = (255, 30, 70)
    green = (11, 218, 81)
    blue = (31, 81, 255)
    orange = (255, 172, 28)
    white = (255, 255, 255)

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


rect1 = pygame.Rect(10, 30, 50, 70)
rect2 = pygame.Rect(70, 30, 50, 70)
polygon_points = (
    (200, 0),
    (WIDTH/2, 0),
    (WIDTH/2, HEIGHT/4),
    (200, HEIGHT/4),
)
def main():
    global run
    cor = [150, 300]
    sign = 1
    while run:
        pygame.draw.rect(WIN, COLORS.white, rect1)
        pygame.draw.rect(WIN, COLORS.white, rect2, 2)
        pygame.draw.circle(WIN, COLORS.red, (40, 150), 30)
        pygame.draw.circle(WIN, COLORS.red, (130, 150), 30, 2)
        pygame.draw.line(WIN, COLORS.blue, (WIDTH, 0), cor, 5)
        pygame.draw.polygon(WIN, COLORS.green, polygon_points)

        # Update vertices of line
        cor[0] += 1 * sign
        cor[1] += 1 * sign
        if (cor[1] > HEIGHT - 2 or cor[0] < 0): sign *= -1
        draw_win()
        events()

main()
