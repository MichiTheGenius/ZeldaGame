import pygame
from player import Player
from settings import *
from tile import Tile
from collectible import Collectible

class Level():
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = CameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.collectible_sprites = pygame.sprite.Group()
        self.rock_image = './assets/rock.png'
        self.sword_image = './assets/sword.png'

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for column_index, column in enumerate(row):
                x = column_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if column == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], self.rock_image)
                elif column == 'p':
                    self.player = Player(
                        (x, y), [self.visible_sprites], self.obstacle_sprites, self.collectible_sprites)
                elif column == 'o':
                    Collectible((x,y), [self.visible_sprites, self.collectible_sprites], self.sword_image)

    def update(self):
        self.visible_sprites.update()
        self.visible_sprites.custom_draw(self.player)


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = SCREEN_WIDTH // 2
        self.half_height = SCREEN_HEIGHT // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            if sprite.is_visible:
                self.display_surface.blit(sprite.image, offset_pos)
