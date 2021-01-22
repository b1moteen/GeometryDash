from constants import *
from exeception import *


def show_intro(screen):
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


def main_menu(screen):
    screen.fill(155, 155, 155)
    y = 0
    level_rects = dict()
    for level in level_names.keys():
        font = pygame.font.Font(None, 50)
        level_name = font.render(level, True, (0, 0, 0))
        screen.blit(level_name, (50, y))
        level_name_rect = level_name.get_rect()
        level_rects[level] = level_name_rect
        y += 50
