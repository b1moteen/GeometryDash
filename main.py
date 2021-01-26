from Camera import *
from views import *
import constants


show_intro(prepare.screen)
player = main_menu(prepare.screen)
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
    prepare.screen.fill("black")
    tiles_group.draw(prepare.screen)
    player_group.draw(prepare.screen)
    pygame.display.flip()
    prepare.clock.tick(FPS)
    if constants.after_death:
        if constants.rerun:
            constants.rerun = False
            constants.after_death = False
            all_sprites.empty()
            tiles_group.empty()
            obstacles_group.empty()
            spikes_group.empty()
            environment_group.empty()
            floor_group.empty()
            finish_group.empty()
            player_group.empty()
            portal_group.empty()
            player = create_level(constants.current_level)
            constants.current_level = None
        elif main_menu:
            constants.main_menu = False
            constants.after_death = False
            all_sprites.empty()
            tiles_group.empty()
            obstacles_group.empty()
            spikes_group.empty()
            environment_group.empty()
            floor_group.empty()
            finish_group.empty()
            player_group.empty()
            portal_group.empty()
            player = views.main_menu(prepare.screen)



