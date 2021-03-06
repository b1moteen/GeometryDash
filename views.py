from Level import *
from exeception import *

pygame.mixer.init()


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
    screen.fill("green")
    font = pygame.font.Font(None, 50)
    first_level_text = font.render("Первый уровень", True, (0, 0, 0))
    screen.blit(first_level_text, (50, 50))
    first_level_text_rect = first_level_text.get_rect()
    first_level_text_rect.x = 50
    first_level_text_rect.y = 50

    second_level_text = font.render("Второй уровень", True, (0, 0, 0))
    screen.blit(second_level_text, (50, 100))
    second_level_text_rect = second_level_text.get_rect()
    second_level_text_rect.x = 50
    second_level_text_rect.y = 100

    exit_text = font.render("Выход", True, (0, 0, 0))
    screen.blit(exit_text, (50, 200))
    exit_text_rect = exit_text.get_rect()
    exit_text_rect.x = 50
    exit_text_rect.y = 200
    """ 
    сюда надо добавлять 
    ваш_уровень_text = font.render("Выход", True, (цвет rgb))
        screen.blit(ваш_уровень_text, (координата x, координата y))
        ваш_уровень_text_rect = exit_text.get_rect()
        ваш_уровень_text_rect.x = координата x
        ваш_уровень_text_rect.y = координата y
    """
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_text_rect.collidepoint(event.pos):
                    terminate()
                elif first_level_text_rect.collidepoint(event.pos):
                    pygame.mixer.music.load("data/music/Stereo Madness.mp3")
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.5)
                    return create_level(level_names["first"])
                elif second_level_text_rect.collidepoint(event.pos):
                    pygame.mixer.music.load("data/music/Back On Track.mp3")
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.5)
                    return create_level(level_names["second"])


def after_death(screen=prepare.screen, level=None):
    pygame.mixer.music.stop()
    screen.fill("black")
    font = pygame.font.Font(None, 50)

    rerun_level_text = font.render("Заново", True, (255, 255, 255))
    screen.blit(rerun_level_text, (50, 50))
    rerun_level_text_rect = rerun_level_text.get_rect()
    rerun_level_text_rect.x = 50
    rerun_level_text_rect.y = 50

    main_menu_level_text = font.render("Главное меню", True, (255, 255, 255))
    screen.blit(main_menu_level_text, (50, 100))
    main_menu_text_rect = main_menu_level_text.get_rect()
    main_menu_text_rect.x = 50
    main_menu_text_rect.y = 100

    exit_text = font.render("Выход", True, (255, 255, 255))
    screen.blit(exit_text, (50, 200))
    exit_text_rect = exit_text.get_rect()
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
                elif rerun_level_text_rect.collidepoint(event.pos):
                    constants.rerun = True
                    constants.current_level = level
                    return
                elif main_menu_text_rect.collidepoint(event.pos):
                    constants.main_menu = True
                    return


def win_menu(screen=prepare.screen, level=None):
    screen.fill("black")
    font = pygame.font.Font(None, 50)

    rerun_level_text = font.render("Заново", True, (255, 255, 255))
    screen.blit(rerun_level_text, (50, 50))
    rerun_level_text_rect = rerun_level_text.get_rect()
    rerun_level_text_rect.x = 50
    rerun_level_text_rect.y = 50

    main_menu_level_text = font.render("Главное меню", True, (255, 255, 255))
    screen.blit(main_menu_level_text, (50, 100))
    main_menu_text_rect = main_menu_level_text.get_rect()
    main_menu_text_rect.x = 50
    main_menu_text_rect.y = 100

    exit_text = font.render("Выход", True, (255, 255, 255))
    screen.blit(exit_text, (50, 300))
    exit_text_rect = exit_text.get_rect()
    exit_text_rect.x = 50
    exit_text_rect.y = 300

    attempts_text = font.render(f"Попытки:{constants.attempts}", True, (255, 255, 255))
    screen.blit(attempts_text, (50, 200))
    attempts_text = exit_text.get_rect()
    attempts_text.x = 50
    attempts_text.y = 200

    coins_text = font.render(f"Монетки:{constants.coins}", True, (255, 255, 255))
    screen.blit(coins_text, (50, 250))
    coins_text = exit_text.get_rect()
    coins_text.x = 50
    coins_text.y = 250

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_text_rect.collidepoint(event.pos):
                    terminate()
                elif rerun_level_text_rect.collidepoint(event.pos):
                    constants.rerun = True
                    constants.current_level = level
                    return
                elif main_menu_text_rect.collidepoint(event.pos):
                    constants.main_menu = True
                    return
