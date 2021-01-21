from constants import *
from Groups import *


class Tile(pygame.sprite.Sprite):
    tile_images = {"background": pygame.image.load("data/ground/background.png"),
                   "box": pygame.image.load("data/ground/box.png"),
                   "floor": pygame.image.load("data/ground/floor.png"),
                   "spike": pygame.image.load("data/ground/spike.png")}

    def __init__(self, tile_type, x, y):
        self.image = Tile.tile_images[tile_type]
        self.image = pygame.transform.scale(self.image, (70, 70))
        if tile_type == "floor":
            super().__init__(all_sprites, tiles_group, floor_group)
        elif tile_type == "background":
            super().__init__(all_sprites, tiles_group, environment_group)
        elif tile_type == "spike":
            super().__init__(all_sprites, tiles_group, spikes_group)
        else:
            super().__init__(all_sprites, tiles_group, obstacles_group)
        self.rect = self.image.get_rect()
        self.rect.x = x * tile_width
        self.rect.y = y * tile_height
