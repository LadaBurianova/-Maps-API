import pygame


def get_image():
    return ''


W, H = 620, 520
size = W, H
FPS = 20
pygame.init()
screen = pygame.display.set_mode(W, H)
run = True
clock = pygame.time.Clock()
image = get_image()

while run:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_PAGEDOWN:
                params['z'] = str(min(13, int(params['z']) + 1))
                image = get_image()
            elif ev.key == pygame.K_PAGEUP:
                params['z'] = str(max(0, int(params['z']) - 1))
                image = get_image()
    screen.fill((0, 0, 0))
    name = get_image()
    image = pygame.image.load(name)
    screen.blit(screen, image, (10, 10))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
