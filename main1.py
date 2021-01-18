import os
import sys

import pygame


def terminate():
    pygame.quit()
    sys.exit()


def show_intro():
    fullname = os.path.join('maps', input_level)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
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


class Tile(pygame.sprite.Sprite):
    tile_images = {"background": pygame.image.load("data/ground/background.png"),
                   "box": pygame.image.load("data/ground/box.png"),
                   "floor": pygame.image.load("data/ground/floor.png"),
                   "spike": pygame.image.load("data/ground/spike.png")}

    def __init__(self, tile_type, x, y):
        if tile_type == "floor":
            super().__init__(all_sprites, tiles_group, floor_group)
        elif tile_type == "background":
            super().__init__(all_sprites, tiles_group, environment_group)
        elif tile_type == "spike":
            super().__init__(all_sprites, tiles_group, spikes_group)
        else:
            super().__init__(all_sprites, tiles_group, obstacles_group)
        self.image = Tile.tile_images[tile_type]
        self.rect = self.image.get_rect()
        self.rect.x = x * tile_width
        self.rect.y = y * tile_height


class Player(pygame.sprite.Sprite):
    player_image = pygame.image.load("data/sprites/square.png")

    def __init__(self, level, x, y):
        super().__init__(all_sprites, player_group)
        self.image = Player.player_image
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = x * tile_width + (tile_width - self.rect.width) // 2
        self.rect.y = y * tile_height + tile_height - self.rect.height
        self.x = x
        self.y = y
        self.level = level
        self.xVelocity = 25
        self.yVelocity = 0

    def update(self):
        mouse_buttons = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP] or mouse_buttons[0]:
            if Player.is_ground(self) or Player.is_on_obstacle(self):
                self.yVelocity -= 10

    def move(self):
        self.rect.x += self.xVelocity
        self.rect.y += self.yVelocity
        if self.yVelocity <= tm and not Player.is_blocking(self):
            self.yVelocity += gravity
        if Player.is_blocking(self):
            self.yVelocity = 0
        Player.death_or_not(self)
        Player.under_ground(self)

    def death_or_not(self):
        for spike in pygame.sprite.spritecollide(self, spikes_group, False):
            if pygame.sprite.collide_mask(self, spike):
                terminate()

        for block in pygame.sprite.spritecollide(self, obstacles_group, False):
            if Player.is_blocking(self):
                if block.rect.x - 2 <= self.rect.x + self.rect.width <= block.rect.x + 2:
                    if not Player.is_on_obstacle(self):
                        terminate()

    def is_blocking(self):
        if self.rect.x < 0 or self.rect.x > 800 or self.rect.y < 0 or self.rect.y > 800:
            return True
        elif pygame.sprite.spritecollide(self, floor_group, False) or pygame.sprite.spritecollide(self, obstacles_group,
                                                                                                  False):
            return True
        else:
            return False

    def is_ground(self):
        if pygame.sprite.spritecollide(self, floor_group, False):
            self.yVelocity = 0
            return True
        else:
            return False

    def is_on_obstacle(self):
        block_collide = pygame.sprite.spritecollide(self, obstacles_group, False)
        if len(block_collide) != 0:
            for block in block_collide:
                if block.rect.y - 10 < self.rect.y + self.rect.height < block.rect.y + 10:
                    self.yVelocity = 0
                    return True

    def under_ground(self):
        if pygame.sprite.spritecollide(self, floor_group, False):
            for floor in pygame.sprite.spritecollide(self, floor_group, False):
                if floor.rect.y > self.rect.y + self.rect.height:
                    self.rect.y = floor.rect.y - self.rect.height - 1


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, sprite):
        sprite.rect.x += self.dx
        sprite.rect.y += self.dy

    def update(self, sprite):
        x, y = sprite.rect.x, sprite.rect.y
        w, h = sprite.rect.width, sprite.rect.height
        self.dx = -(x - width // 2 + w // 2 + 200)
        self.dy = -(y - height // 2 + h // 2 - 200)


def load_level(filename):
    with open("maps/" + filename) as file:
        level = list(map(str.strip, file))
        max_len = len(max(level, key=len))
        level = list(map(lambda line: list(line.ljust(max_len, ".")), level))
        return level


def create_level(filename):
    level = load_level(filename)
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == ".":
                Tile("background", x, y)
            if level[y][x] == "#":
                Tile("box", x, y)
            elif level[y][x] == "@":
                level[y][x] = "."
                Tile("background", x, y)
                player = Player(level, x, y)
            elif level[y][x] == "-":
                Tile("floor", x, y)
            elif level[y][x] == "+":
                level[y][x] = "."
                Tile("background", x, y)
                level[y][x] = "+"
                Tile("spike", x, y)

    return player


input_level = "first_map.txt"
pygame.init()
size = width, height = 800, 800
tile_width = 50
tile_height = 50
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Перемещение героя")
clock = pygame.time.Clock()
FPS = 120
gravity = 0.7
tm = 50  # Terminal Velocity

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
obstacles_group = pygame.sprite.Group()
spikes_group = pygame.sprite.Group()
environment_group = pygame.sprite.Group()
floor_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

show_intro()
player = create_level(input_level)
camera = Camera()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    player.move()
    player_group.update()
    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)
    screen.fill("black")
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
