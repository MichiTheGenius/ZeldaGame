import pygame
from settings import *
from input import Input
from debug import debug
from sprite import Sprite

class Player(Sprite):
    def __init__(self, pos, groups, image_path, obstacle_sprites, collectible_sprites):
        super().__init__(pos, groups, image_path)

        self.collectible_count = 0

        self.direction = pygame.math.Vector2()
        self.display_surface = pygame.display.get_surface()
        self.input = Input()

        self.obstacle_sprites = obstacle_sprites
        self.collectible_sprites = collectible_sprites

    def update(self):
        self.input.update()
        self.move()
        self.collect_collectible()

    def collect_collectible(self):
        for sprite in self.collectible_sprites:
            if self.rect.colliderect(sprite.rect) and sprite.can_collect:
                self.collectible_count += 1
                sprite.can_collect = False
                sprite.is_visible = False
        debug(self.collectible_count)

    def check_collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:  # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:  # moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:  # moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:  # moving up
                        self.rect.top = sprite.rect.bottom

    def move(self):
        if self.input.left():
            self.direction.x = -1
        elif self.input.right():
            self.direction.x = 1
        else:
            self.direction.x = 0

        if self.input.up():
            self.direction.y = -1
        elif self.input.down():
            self.direction.y = 1
        else:
            self.direction.y = 0

        # normalize the direction so that we move with the same speed diagonally
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * PLAYER_SPEED
        self.check_collision('horizontal')
        self.rect.y += self.direction.y * PLAYER_SPEED
        self.check_collision('vertical')
