from Camera import *
from views import *
from prepare import *
from exeception import *

show_intro(screen)
player = main_menu(screen)
camera = Camera()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    player_group.update()
    for sprite in player_group:
        camera.update(sprite)
    for sprite in all_sprites:
        camera.apply(sprite)
    screen.fill("black")
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
