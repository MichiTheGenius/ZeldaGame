import pygame

class Collectible(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('./assets/sword.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.display_image = True
        self.can_collect = True