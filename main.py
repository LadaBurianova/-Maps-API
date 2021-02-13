import pygame
import requests
import sys
from io import BytesIO

COLOR_ACTIVE = (255, 204, 0)
COLOR_INACTIVE = (58, 117, 196)


def change_color(box, ev, active):
    if box.collidepoint(ev.pos):
        active = not active
    else:
        active = False
    color = COLOR_ACTIVE if active else COLOR_INACTIVE
    return active, color


def get_image():
    api_server = 'https://static-maps.yandex.ru/1.x/?'
    response = requests.get(api_server, params)
    if not response:
        print("Http статус:", response.status_code, "(", response.text, ")")
        sys.exit(response.status_code)
    return pygame.image.load(BytesIO(response.content))


params = {'ll': '133.795384,-25.694768',
          'z': '4',
          'l': 'sat',
          'size': '500,400'}

W, H = size = 620, 520
FPS = 20
pygame.init()
screen = pygame.display.set_mode(size)
run = True
clock = pygame.time.Clock()

input_box = pygame.Rect(10, 410, 150, 32)
text = ''
color = COLOR_INACTIVE
active = False

while run:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_PAGEDOWN:
                params['z'] = str(min(13, int(params['z']) + 1))
            elif ev.key == pygame.K_PAGEUP:
                params['z'] = str(max(0, int(params['z']) - 1))
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            active, color = change_color(input_box, ev, active)
    screen.fill((0, 0, 0))
    image = get_image()
    screen.blit(image, (10, 10))
    pygame.draw.rect(screen, color, input_box, 2)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
