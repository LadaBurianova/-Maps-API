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
        elif ev.type == pygame.KEYDOWN:
            if ev.mod == pygame.K_PAGEDOWN:
                params['z'] += 1
            elif ev.mod == pygame.K_PAGEUP:
                params['z'] -= 1
            elif ev.key == pygame.K_UP:
                pass
    screen.fill((0, 0, 0))
    name = get_image()
    image = pygame.image.load(name)
    screen.blit(screen, image, (10, 10))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
