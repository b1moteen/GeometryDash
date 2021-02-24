import prepare

# Разрешение игры

# constants
size = width, height = prepare.display_w, prepare.display_h
FPS = 60
gravity = 1
tm = 20
tm_plain = 10
default_jump = 17
default_plain_jump = 2.5
delta_y = 25
delta_x = 10
floor_delta_y = 10
plain_delta_y = 45
magic_number = 12

tile_width = 70 * prepare.display_w // 1920

tile_height = 70 * prepare.display_h // 1080

# --------

rerun = False
main_menu = False
current_level = False
after_death = False
# level_names
# это надо изменять для добавления уровня
level_names = {'first': "first_level.txt",
               "second": "second_level.txt"}
# это надо изменять для добавления уровня
level_music = {
    'first_level.txt': "data/music/Stereo Madness.mp3",
    "second_level.txt": "data/music/Back On Track.mp3"
}
attempts = 1
coins = 0
# pause = False
# velocities = [0, 0]
