import ctypes

# Разрешение игры
user32 = ctypes.windll.user32
display_w = user32.GetSystemMetrics(0)
display_h = user32.GetSystemMetrics(1)

# constants
size = width, height = display_w, display_h
FPS = 60
gravity = 1
tm = 20
tm_plain = 10

tile_width = 70 * display_w // 1920

tile_height = 70 * display_h // 1080

# --------

square_x_velocity = 2

# level_names

level_names = {'first': "first_level.txt",
               "second": "second_level.txt"}
