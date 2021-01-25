import Level
import views
from Groups import *
from constants import *
from exeception import *
from prepare import *


class Square(pygame.sprite.Sprite):
    player_image = pygame.image.load("data/sprites/square.png")

    def __init__(self, level, level_name, x, y):
        player_group.empty()
        super().__init__(all_sprites, player_group)
        self.image = Square.player_image
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = x * tile_width
        self.rect.y = (y - 1) * tile_height
        self.level = level
        self.level_name = level_name
        self.x = x
        self.y = y
        self.xVelocity = 8
        self.yVelocity = 0

    def update(self):
        mouse_buttons = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP] or mouse_buttons[0]:
            if Square.is_ground(self) or Square.is_on_obstacle(self):
                self.yVelocity -= 17

        self.rect.x += self.xVelocity
        self.rect.y += self.yVelocity
        if self.yVelocity <= tm and not Square.is_blocking(self):
            self.yVelocity += gravity
        if Square.is_blocking(self):
            self.yVelocity = 0
        self.y = self.rect.y // tile_height
        Square.death_or_not(self)
        Square.under_ground(self)
        Square.plain_portal(self)
        Square.finish(self)

    def death_or_not(self):
        for spike in pygame.sprite.spritecollide(self, spikes_group, False):
            if pygame.sprite.collide_mask(self, spike):
                if views.after_death(screen, self.level_name) == "rerun":
                    player = Level.create_level(self.level_name)
                elif views.after_death(screen, self.level_name) == "main_menu":
                    views.main_menu(screen)

        for block in pygame.sprite.spritecollide(self, obstacles_group, False):
            if Square.is_blocking(self):
                if block.rect.x - 5 <= self.rect.x + self.rect.width <= block.rect.x + 5 and not Square.is_on_obstacle(
                        self):
                    if views.after_death(screen, self.level_name) == "rerun":
                        player = Level.create_level(self.level_name)
                    elif views.after_death(screen, self.level_name) == "main_menu":
                        views.main_menu(screen)

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
                if block.rect.y - 17 <= self.rect.y + self.rect.height <= block.rect.y + 17:
                    if self.rect.y % 70 <= 17:
                        y_pos = self.rect.y // 70
                        self.rect.y = y_pos * 70
                    return True

    def under_ground(self):
        if pygame.sprite.spritecollide(self, floor_group, False):
            if self.rect.y % 70 < 20:
                y_pos = self.rect.y // 70
                self.rect.y = y_pos * 70
                return True

    def plain_portal(self):
        if pygame.sprite.spritecollide(self, portal_group, False):
            Plain(self.level, self.level_name, self.x, self.y)

    def finish(self):
        if pygame.sprite.spritecollide(self, finish_group, False):
            print("Ты выиграл")
            terminate()


class Plain(pygame.sprite.Sprite):
    player_image = pygame.image.load("data/sprites/plane.png")

    def __init__(self, level, level_name, x, y):
        player_group.empty()
        super().__init__(all_sprites, player_group)
        self.image = Plain.player_image
        self.rect = self.image.get_rect()
        self.rect.x = x * tile_width
        self.rect.y = (y - 1) * tile_height
        self.level = level
        self.level_name = level_name
        self.x = x
        self.y = y
        self.xVelocity = 10
        self.yVelocity = 0
        self.gravity = 1.5

    def update(self):
        mouse_buttons = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP] or mouse_buttons[0]:
            self.yVelocity -= 2.5
        self.rect.x += self.xVelocity
        self.rect.y += self.yVelocity
        if self.yVelocity <= tm_plain and not Plain.is_blocking(self):
            self.yVelocity += self.gravity
        if Plain.is_on_obstacle(self) or Plain.is_ground(self):
            self.yVelocity = 0
        self.y = self.rect.y // tile_height
        Plain.death_or_not(self)
        Plain.under_ground(self)
        Plain.square_portal(self)
        Plain.finish(self)

    def death_or_not(self):
        for spike in pygame.sprite.spritecollide(self, spikes_group, False):
            if pygame.sprite.collide_mask(self, spike):
                if views.after_death(screen, self.level_name) == "rerun":
                    player = Level.create_level(self.level_name)
                elif views.after_death(screen, self.level_name) == "main_menu":
                    views.main_menu(screen)

        for block in pygame.sprite.spritecollide(self, obstacles_group, False):
            if Plain.is_blocking(self):
                if block.rect.x - 10 <= self.rect.x + self.rect.width <= block.rect.x + 10 and not Plain.is_on_obstacle(
                        self):
                    if views.after_death(screen, self.level_name) == "rerun":
                        player = Level.create_level(self.level_name)
                    elif views.after_death(screen, self.level_name) == "main_menu":
                        views.main_menu(screen)

    def is_blocking(self):
        if self.rect.x < 0 or self.rect.x > 1920 or self.rect.y > 1080:
            return True
        elif self.rect.y <= 0:
            self.rect.y = 15
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
                if block.rect.y - 45 < self.rect.y + self.rect.height < block.rect.y + 45:
                    if self.rect.y % 70 < 25:
                        y_pos = self.rect.y // 70
                        self.rect.y = y_pos * 70
                    return True

    def under_ground(self):
        if pygame.sprite.spritecollide(self, floor_group, False):
            if self.rect.y % 70 < 25:
                y_pos = self.rect.y // 70
                self.rect.y = y_pos * 70

    def square_portal(self):
        if pygame.sprite.spritecollide(self, portal_group, False):
            Square(self.level, self.level_name, self.x, self.y)

    def finish(self):
        if pygame.sprite.spritecollide(self, finish_group, False):
            print("Ты выиграл")
            terminate()
