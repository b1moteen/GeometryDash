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
        constants.after_death = False
        constants.coins = 0
        all_sprites.empty()
        tiles_group.empty()
        obstacles_group.empty()
        spikes_group.empty()
        environment_group.empty()
        floor_group.empty()
        finish_group.empty()
        player_group.empty()
        portal_group.empty()
        if constants.rerun:
            pygame.mixer.music.load(constants.level_music[constants.current_level])
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.5)
            constants.rerun = False
            player = create_level(constants.current_level)
            constants.current_level = None
        elif main_menu:
            constants.main_menu = False
            constants.attempts = 1
            player = views.main_menu(prepare.screen)




