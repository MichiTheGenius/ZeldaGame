import pygame
import sys
from settings import *
from square import Square


class Game():
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('myGame')

        self.clock = pygame.time.Clock()

        self.my_square = Square(0, 0, 100, RED)
        self.my_square.set_vel_x(1)
        self.my_square.set_vel_y(2)

    def mainloop(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(BLACK)

            self.my_square.update()
            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


g = Game()
g.mainloop()
