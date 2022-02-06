import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, groups, image_path):
        super().__init__(groups)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.is_visible = True
