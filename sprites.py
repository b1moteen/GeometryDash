import Groups
import constants
import prepare
import views
from exeception import *


class Square(pygame.sprite.Sprite):
    player_image = pygame.image.load("data/sprites/square.png")

    def __init__(self, level, level_name, x, y):
        Groups.player_group.empty()
        super().__init__(Groups.all_sprites, Groups.player_group)
        self.image = Square.player_image
        self.image = pygame.transform.scale(self.image, (constants.tile_width, constants.tile_height))
        self.rect = self.image.get_rect()
        self.rect.x = x * constants.tile_width
        self.rect.y = (y - 1) * constants.tile_height
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
                self.yVelocity -= constants.default_jump

        # if keys[pygame.K_ESCAPE] and not constants.pause:
        #     constants.velocities = [self.xVelocity, self.yVelocity]
        #     self.xVelocity = 0
        #     self.yVelocity = 0
        #     constants.pause = True
        #
        # if keys[pygame.K_ESCAPE] and constants.pause:
        #     self.xVelocity = constants.velocities[0]
        #     self.yVelocity = constants.velocities[1]

        self.rect.x += self.xVelocity
        self.rect.y += self.yVelocity
        if self.yVelocity <= constants.tm and not Square.is_blocking(self):
            self.yVelocity += constants.gravity
        if Square.is_blocking(self):
            self.yVelocity = 0
        self.y = self.rect.y // constants.tile_height
        Square.collect_coin(self)
        Square.death_or_not(self)
        Square.under_ground(self)
        Square.plain_portal(self)
        Square.finish(self)

    def death_or_not(self):
        for spike in pygame.sprite.spritecollide(self, Groups.spikes_group, False):
            if pygame.sprite.collide_mask(self, spike):
                constants.after_death = True
                pygame.mixer.music.pause()
                constants.attempts += 1
                views.after_death(prepare.screen, self.level_name)

        for kill_box in pygame.sprite.spritecollide(self, Groups.kill_obstacle_group, False):
            if pygame.sprite.collide_mask(self, kill_box):
                constants.after_death = True
                constants.attempts += 1
                pygame.mixer.music.pause()
                views.after_death(prepare.screen, self.level_name)

        for block in pygame.sprite.spritecollide(self, Groups.obstacles_group, False):
            if Square.is_blocking(self):
                if block.rect.x - constants.delta_x <= self.rect.x + self.rect.width <= block.rect.x + constants.delta_x and \
                        not Square.is_on_obstacle(self):
                    constants.after_death = True
                    pygame.mixer.music.pause()
                    constants.attempts += 1
                    views.after_death(prepare.screen, self.level_name)

        for floor in pygame.sprite.spritecollide(self, Groups.floor_group, False):
            if Square.is_blocking(self):
                if floor.rect.y - constants.floor_delta_y > self.rect.y + self.rect.height and \
                        not Square.is_on_obstacle(self):
                    constants.after_death = True
                    pygame.mixer.music.pause()
                    constants.attempts += 1
                    views.after_death(prepare.screen, self.level_name)

    def is_blocking(self):
        if self.rect.x < 0 or self.rect.x > constants.width or self.rect.y < 0 or self.rect.y > constants.height:
            return True
        elif pygame.sprite.spritecollide(self, Groups.floor_group, False) or \
                pygame.sprite.spritecollide(self, Groups.obstacles_group, False):
            return True
        else:
            return False

    def is_ground(self):
        if pygame.sprite.spritecollide(self, Groups.floor_group, False):
            self.yVelocity = 0
            return True
        else:
            return False

    def is_on_obstacle(self):
        block_collide = pygame.sprite.spritecollide(self, Groups.obstacles_group, False)
        if len(block_collide) != 0:
            for block in block_collide:
                if block.rect.y - constants.delta_y <= self.rect.y + self.rect.height <= block.rect.y + constants.delta_y:
                    if self.rect.y % constants.tile_height <= constants.delta_y:
                        y_pos = self.rect.y // constants.tile_height
                        self.rect.y = y_pos * constants.tile_height
                    return True

    def under_ground(self):
        floor_collide = pygame.sprite.spritecollide(self, Groups.floor_group, False)
        if len(floor_collide) != 0:
            for floor in floor_collide:
                if floor.rect.y - constants.delta_y <= self.rect.y + self.rect.height <= floor.rect.y + constants.delta_y:
                    if self.rect.y % constants.tile_height <= constants.delta_y:
                        y_pos = self.rect.y // constants.tile_height
                        self.rect.y = y_pos * constants.tile_height
                    return True

    def plain_portal(self):
        if pygame.sprite.spritecollide(self, Groups.portal_group, False):
            Plain(self.level, self.level_name, self.x, self.y)

    def finish(self):
        if pygame.sprite.spritecollide(self, Groups.finish_group, False):
            constants.win = True
            pygame.mixer.music.stop()
            views.win_menu(prepare.screen, self.level_name)

    def collect_coin(self):
        if pygame.sprite.spritecollide(self, Groups.coin_group, True):
            collect_coin = pygame.mixer.Sound('data/music/collect_coin.mp3')
            collect_coin.play()
            collect_coin.set_volume(0.5)
            constants.coins += 1


class Plain(pygame.sprite.Sprite):
    player_image = pygame.image.load("data/sprites/plane.png")

    def __init__(self, level, level_name, x, y):
        Groups.player_group.empty()
        super().__init__(Groups.all_sprites, Groups.player_group)
        self.image = Plain.player_image
        self.rect = self.image.get_rect()
        self.rect.x = x * constants.tile_width
        self.rect.y = y * constants.tile_height
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
            self.yVelocity -= constants.default_plain_jump
        self.rect.x += self.xVelocity
        self.rect.y += self.yVelocity
        if self.yVelocity <= constants.tm_plain and not Plain.is_blocking(self):
            self.yVelocity += self.gravity
        if Plain.is_on_obstacle(self) or Plain.is_ground(self):
            self.yVelocity = 0
        self.y = self.rect.y // constants.tile_height
        Plain.collect_coin(self)
        Plain.death_or_not(self)
        Plain.under_ground(self)
        Plain.square_portal(self)
        Plain.finish(self)

    def death_or_not(self):
        for spike in pygame.sprite.spritecollide(self, Groups.spikes_group, False):
            if pygame.sprite.collide_mask(self, spike):
                constants.after_death = True
                constants.attempts += 1
                pygame.mixer.music.pause()
                views.after_death(prepare.screen, self.level_name)

        for kill_box in pygame.sprite.spritecollide(self, Groups.kill_obstacle_group, False):
            if pygame.sprite.collide_mask(self, kill_box):
                constants.after_death = True
                constants.attempts += 1
                pygame.mixer.music.pause()
                views.after_death(prepare.screen, self.level_name)

        for block in pygame.sprite.spritecollide(self, Groups.obstacles_group, False):
            if Plain.is_blocking(self):
                if block.rect.x - constants.delta_x <= self.rect.x + self.rect.width <= block.rect.x + constants.delta_x and not Plain.is_on_obstacle(
                        self):
                    constants.after_death = True
                    constants.attempts += 1
                    pygame.mixer.music.pause()
                    views.after_death(prepare.screen, self.level_name)

    def is_blocking(self):
        if self.rect.x < 0 or self.rect.x > constants.width or self.rect.y > constants.height:
            return True
        elif self.rect.y <= 0:
            self.rect.y = 15
            return True
        elif pygame.sprite.spritecollide(self, Groups.floor_group, False) or \
                pygame.sprite.spritecollide(self, Groups.obstacles_group, False):
            return True
        else:
            return False

    def is_ground(self):
        if pygame.sprite.spritecollide(self, Groups.floor_group, False):
            self.yVelocity = 0
            return True
        else:
            return False

    def is_on_obstacle(self):
        block_collide = pygame.sprite.spritecollide(self, Groups.obstacles_group, False)
        if len(block_collide) != 0:
            for block in block_collide:
                if block.rect.y - constants.plain_delta_y < self.rect.y + self.rect.height < block.rect.y + constants.plain_delta_y:
                    if self.rect.y % constants.tile_height < constants.delta_y:
                        y_pos = self.rect.y // constants.tile_height
                        self.rect.y = y_pos * constants.tile_height
                    return True

    def under_ground(self):
        floor_collide = pygame.sprite.spritecollide(self, Groups.floor_group, False)
        if len(floor_collide) != 0:
            for floor in floor_collide:
                if floor.rect.y - constants.delta_y <= self.rect.y + self.rect.height <= floor.rect.y + constants.delta_y:
                    if self.rect.y % constants.tile_height <= constants.delta_y:
                        y_pos = self.rect.y // constants.tile_height
                        self.rect.y = y_pos * constants.tile_height
                    return True

    def square_portal(self):
        if pygame.sprite.spritecollide(self, Groups.portal_group, False):
            Square(self.level, self.level_name, self.x, self.y)

    def finish(self):
        if pygame.sprite.spritecollide(self, Groups.finish_group, False):
            constants.win = True
            pygame.mixer.music.stop()
            views.win_menu(prepare.screen, self.level_name)

    def collect_coin(self):
        if pygame.sprite.spritecollide(self, Groups.coin_group, True):
            collect_coin = pygame.mixer.Sound("data/music/collect_coin.mp3")
            collect_coin.play()
            collect_coin.set_volume(0.5)
            constants.coins += 1
