from Groups import *
from constants import *
from exeception import *


class Player(pygame.sprite.Sprite):
    player_image = pygame.image.load("data/sprites/square.png")

    def __init__(self, level, x, y):
        super().__init__(all_sprites, player_group)
        self.image = Player.player_image
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = x * tile_width
        self.rect.y = y * tile_height
        self.x = x
        self.y = y
        self.level = level
        self.xVelocity = 8
        self.yVelocity = 0

    def update(self):
        mouse_buttons = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP] or mouse_buttons[0]:
            if Player.is_ground(self) or Player.is_on_obstacle(self):
                self.yVelocity -= 15

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
                if block.rect.x - 5 <= self.rect.x + self.rect.width <= block.rect.x + 5 and not Player.is_on_obstacle(
                        self):
                    terminate()

    def is_blocking(self):
        if self.rect.x < 0 or self.rect.x > 1920 or self.rect.y < 0 or self.rect.y > 1080:
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
                    if self.rect.y % 70 < 5:
                        y_pos = self.rect.y // 70
                        self.rect.y = y_pos * 70
                    return True

    def under_ground(self):
        if pygame.sprite.spritecollide(self, floor_group, False):
            for floor in pygame.sprite.spritecollide(self, floor_group, False):
                if floor.rect.y > self.rect.y + self.rect.height:
                    self.rect.y = self.y * tile_height + tile_height - self.rect.height
