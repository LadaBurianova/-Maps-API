import pygame
import requests
import sys
from io import BytesIO

pygame.init()
COLOR_ACTIVE = (255, 204, 0)
COLOR_INACTIVE = (58, 117, 196)
INPUT_FONT = pygame.font.Font(None, 32)
API_SERVER = 'https://static-maps.yandex.ru/1.x/?'


def change_color(box, ev, active):
    if box.collidepoint(ev.pos):
        active = not active
    else:
        active = False
    color = COLOR_ACTIVE if active else COLOR_INACTIVE
    return active, color


def get_image(response):
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
screen = pygame.display.set_mode(size)
run = True
clock = pygame.time.Clock()

input_box = pygame.Rect(10, 410, 150, 32)
text = ''
color = COLOR_INACTIVE
active = False
response = requests.get(API_SERVER, params)
image = get_image(response)

while run:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
        elif ev.type == pygame.KEYDOWN:
            if ev.type == pygame.KEYDOWN:
                if active:
                    if ev.key == pygame.K_RETURN:
                        if text != '':
                            try:
                                response = requests.get(text)
                                image = get_image(response)
                            except Exception:
                                response = requests.get(API_SERVER, params)
                                text = ''
                    elif ev.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += ev.unicode
            if ev.key == pygame.K_PAGEDOWN:
                params['z'] = str(min(13, int(params['z']) + 1))
                response = requests.get(API_SERVER, params)
                image = get_image(response)
            elif ev.key == pygame.K_PAGEUP:
                params['z'] = str(max(0, int(params['z']) - 1))
                response = requests.get(API_SERVER, params)
                image = get_image(response)
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            active, color = change_color(input_box, ev, active)
    screen.fill((0, 0, 0))
    screen.blit(image, (10, 10))
    txt_surface = INPUT_FONT.render(text, True, color)
    input_box.w = max(200, txt_surface.get_width() + 10)
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, color, input_box, 2)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
