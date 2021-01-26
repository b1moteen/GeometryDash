import pygame

from constants import display_w, display_h

pygame.init()
screen = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption("Geometry Dash")
clock = pygame.time.Clock()
