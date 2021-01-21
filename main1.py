import os

from Camera import *
from Level import *
from exeception import *
from sprites import *


def show_intro():
    fullname = os.path.join('maps', input_level)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    intro_screen = pygame.image.load("data/fon.jpg")
    intro_screen = pygame.transform.scale(intro_screen, (1920, 1080))
    screen.blit(intro_screen, (0, 0))
    font = pygame.font.Font(None, 50)
    game_text = font.render("Играть", True, (0, 0, 0))
    exit_text = font.render("Выход", True, (0, 0, 0))
    screen.blit(game_text, (50, 100))
    screen.blit(exit_text, (50, 200))
    # определяем прямоугольники в которых находятся надписи
    game_text_rect = game_text.get_rect()
    game_text_rect.x = 50
    game_text_rect.y = 100

    exit_text_rect = game_text.get_rect()
    exit_text_rect.x = 50
    exit_text_rect.y = 200
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_text_rect.collidepoint(event.pos):
                    terminate()
                elif game_text_rect.collidepoint(event.pos):
                    return


input_level = "first_map.txt"
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Geometry Dash")
clock = pygame.time.Clock()

show_intro()
player = create_level(input_level)
camera = Camera()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    player.move()
    player_group.update()
    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)
    screen.fill("black")
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
