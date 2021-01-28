from constants import *
from Groups import *


class Tile(pygame.sprite.Sprite):
    tile_images = {"background": pygame.image.load("data/ground/background.png"),
                   "box": pygame.image.load("data/ground/box.png"),
                   "floor": pygame.image.load("data/ground/floor.png"),
                   "spike": pygame.image.load("data/ground/spike.png"),
                   "portal": pygame.image.load("data/ground/portal.png"),
                   "finish": pygame.image.load("data/ground/background.png"),
                   "reverse_spike": pygame.image.load("data/ground/reverse_spike.png"),
                   "kill_box": pygame.image.load("data/ground/box.png")}

    def __init__(self, tile_type, x, y):
        self.image = Tile.tile_images[tile_type]
        if tile_type == "floor":
            super().__init__(all_sprites, tiles_group, floor_group)
        elif tile_type == "background":
            super().__init__(all_sprites, tiles_group, environment_group)
        elif tile_type == "spike" or tile_type == 'reverse_spike':
            super().__init__(all_sprites, tiles_group, spikes_group)
        elif tile_type == "portal":
            super().__init__(all_sprites, tiles_group, environment_group, portal_group)
        elif tile_type == "finish":
            super().__init__(all_sprites, tiles_group, finish_group)
        elif tile_type == "kill_box":
            super().__init__(all_sprites, tiles_group, kill_obstacle_group)
        else:
            super().__init__(all_sprites, tiles_group, obstacles_group)

        self.rect = self.image.get_rect()
        self.rect.x = x * tile_width
        self.rect.y = y * tile_height
