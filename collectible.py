import pygame
from tile import Tile

class Collectible(Tile):
    def __init__(self, pos, groups, image_path):
        super().__init__(pos, groups, image_path)
        self.can_collect = True