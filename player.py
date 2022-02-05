import pygame
from settings import *
from input import Input

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites) -> None:
        super().__init__(groups)
        self.image = pygame.image.load('./assets/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction = pygame.math.Vector2()
        self.display_surface = pygame.display.get_surface()
        self.input = Input() 

        self.obstacle_sprites = obstacle_sprites

    def update(self):
        self.input.update()
        self.move()
    
    def check_collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: # moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: # moving up
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

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * PLAYER_SPEED
        self.check_collision('horizontal')
        self.rect.y += self.direction.y * PLAYER_SPEED
        self.check_collision('vertical')