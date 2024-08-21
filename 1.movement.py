import pygame

pygame.init()
SCREEN_W = 800
SCREEN_H = 600
run = True

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

player = pygame.Rect((300, 250, 50, 50))
while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a]: player.move_ip(-1, 0)
    elif key[pygame.K_d]: player.move_ip(1, 0)
    elif key[pygame.K_w]: player.move_ip(0, -1)
    elif key[pygame.K_s]: player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
