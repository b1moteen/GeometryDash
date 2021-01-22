import os

from Camera import *
from Level import *
from sprites import *
from views import *


input_level = "first_map.txt"
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Geometry Dash")
clock = pygame.time.Clock()

show_intro(screen)
player = create_level(input_level)
camera = Camera()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    player_group.update()
    for sprite in player_group:
        camera.update(sprite)
    for sprite in all_sprites:
        camera.apply(sprite)
    screen.fill("black")
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
