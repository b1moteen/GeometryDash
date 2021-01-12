import pygame
import sys
import pytmx

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 480, 480
FPS = 60
MAPS_DIR = 'maps'


def terminate():
    pygame.quit()
    sys.exit()


class GameMap:

    def __init__(self, filename, free_tiles, finish_tile):
        super().__init__(all_sprites, tiles_group)
        self.map = pytmx.load_pygame(f"{MAPS_DIR}/{filename}")
        self.height = self.map.height
        self.width = self.map.width
        self.tile_size = self.map.tilewidth
        self.free_tiles = free_tiles
        self.finish_tile = finish_tile

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 0)
                screen.blit(image, (x * self.tile_size, y * self.tile_size))

    def get_tile_id(self, position):
        return self.map.tiledgidmap[self.map.get_tile_gid(*position, 0)]

    def is_free(self, position):
        return self.get_tile_id(position) in self.free_tiles


class MainHero:

    def __init__(self, pic, position):
        super().__init__(all_sprites, player_group)
        self.image = pygame.image.load(f"data/{pic}")
        self.x, self.y = position[0], position[1]

    def get_position(self):
        return self.x, self.y

    def set_position(self, position):
        self.x, self.y = position

    def render(self, screen):
        screen.blit(self.image, self.x * self.tile_size, self.y * self.tile_size)


class Game:

    def __init__(self, map, hero):
        self.map = map
        self.hero = hero

    def render(self, screen):
        self.map.render(screen)
        self.hero.render(screen)

    def update_hero(self):
        pass

    def check_win(self):
        return self.map.get_tile_id(self.hero.get_position()) == self.map.finish_tile

    def check_lose(self):
        pass


pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Geometry Dash")



clock = pygame.time.Clock()
runnung = True
game_over = False
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

map = GameMap("first_map.tmx", [2, 35, 222], 222)
hero = MainHero('quadrat.png', [90, 90])
game = Game(map, hero)
while runnung:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    screen.fill((0, 0, 0))
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

