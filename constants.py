import prepare

# Разрешение игры

# constants
size = width, height = prepare.display_w, prepare.display_h
FPS = 60
gravity = 1
tm = 20
tm_plain = 10

tile_width = 70 * prepare.display_w // 1920

tile_height = 70 * prepare.display_h // 1080

# --------

rerun = False
main_menu = False
current_level = False
after_death = False
# level_names

level_names = {'first': "first_level.txt",
               "second": "second_level.txt"}

level_music = {
    'first': "data/music/Stereo Madness.mp3",
    "second": "data/music/Back On Track.mp3"
}
attempts = 1
