import pygame
import constants

pygame.init()
screen = pygame.display.set_mode()
display_w = screen.get_rect().size[0]
display_h = screen.get_rect().size[1]
pygame.display.set_caption("Geometry Dash")
clock = pygame.time.Clock()
