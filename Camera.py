from constants import *

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
        self.dy = -(y - height // 2 + h // 2 - 450)
        if self.dy > -12:
            self.dy = 0

