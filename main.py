import pygame


def get_image():
    return ''


W, H = 620, 520
FPS = 20
pygame.init()
screen = pygame.display.set_mode(W, H)
run = True
clock = pygame.time.Clock()

while run:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
    screen.fill((0, 0, 0))
    name = get_image()
    image = pygame.image.load(name)
    screen.blit(screen, image, (10, 10))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
