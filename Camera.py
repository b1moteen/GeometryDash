import constants


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
        self.dx = -(x - constants.width // 2 + w // 2 + 200 * constants.width // 1920)
        self.dy = -(y - constants.height // 2 + h // 2 - 450 * constants.height // 1080)
        if self.dy > -constants.magic_number:
            self.dy = 0

