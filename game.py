import pygame
import sys
from settings import *
from square import Square
from input import Input


class Game():
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('myGame')

        self.clock = pygame.time.Clock()

        self.input = Input()

        self.my_square = Square(0, 0, 100, RED)

    def square_movement(self):
        if self.input.left():
            self.my_square.set_vel_x(-VELOCITY_X)
        elif self.input.right():
            self.my_square.set_vel_x(VELOCITY_X)
        else:
            self.my_square.set_vel_x(0)

        if self.input.up():
            self.my_square.set_vel_y(-VELOCITY_Y)
        elif self.input.down():
            self.my_square.set_vel_y(VELOCITY_Y)
        else:
            self.my_square.set_vel_y(0)

    def update(self):
        self.input.update()
        self.square_movement()
        self.my_square.update()

    def mainloop(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(BLACK)

            self.update()

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


g = Game()
g.mainloop()
