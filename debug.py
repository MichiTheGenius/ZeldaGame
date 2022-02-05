import pygame
from settings import *

def debug(info):
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 16)
    text_surface = font.render(str(info), False, WHITE)
    display_surface = pygame.display.get_surface()
    display_surface.blit(text_surface, (10,10))
