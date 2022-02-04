import pygame
from settings import *
from input import Input


class Player:
    def __init__(self) -> None:
        self.position = pygame.math.Vector2()
        self.direction = pygame.math.Vector2()
        self.display_surface = pygame.display.get_surface()
        self.input = Input()

    def update(self):
        self.input.update()
        self.move()
        self.draw()

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
        self.position += self.direction * PLAYER_SPEED

    def draw(self):
        pygame.draw.rect(self.display_surface, (0, 0, 0),
                         (self.position.x, self.position.y, 40, 40))
