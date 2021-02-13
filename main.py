import pygame
import requests
import sys
from io import BytesIO


def get_image():
    api_server = 'https://static-maps.yandex.ru/1.x/?'
    response = requests.get(api_server, params)
    if not response:
        print("Http статус:", response.status_code, "(", response.text, ")")
        sys.exit(response.status_code)
    return pygame.image.load(BytesIO(response.content))


params = {'ll': '133.795384,-25.694768',
          'z': '4',
          'l': 'sat'}

W, H = 620, 520
size = W, H
FPS = 20
pygame.init()
screen = pygame.display.set_mode(size)
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
            elif ev.key == pygame.K_PAGEUP:
                params['z'] = str(max(0, int(params['z']) - 1))
            elif ev.key == pygame.K_RIGHT:
                l1, l2 = tuple(map(float, params['ll'].split(',')))
                l1 += 1 * int(params['z'])
                if l1 >= 180:
                    l1 = 0
                params['ll'] = ','.join([str(l1), str(l2)])
            elif ev.key == pygame.K_LEFT:
                l1, l2 = tuple(map(float, params['ll'].split(',')))
                l1 -= 1 * int(params['z'])
                if l1 <= 0:
                    l1 = 180
                params['ll'] = ','.join([str(l1), str(l2)])
            elif ev.key == pygame.K_UP:
                l1, l2 = tuple(map(float, params['ll'].split(',')))
                l2 = min(l2 + 1 * int(params['z']), 180)
                params['ll'] = ','.join([str(l1), str(l2)])
            elif ev.key == pygame.K_DOWN:
                l1, l2 = tuple(map(float, params['ll'].split(',')))
                l2 = max(l2 - 1 * int(params['z']), 0)
                params['ll'] = ','.join([str(l1), str(l2)])
            image = get_image()
    screen.fill((0, 0, 0))
    screen.blit(image, (10, 10))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
