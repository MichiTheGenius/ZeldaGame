import pygame
import sys
from level import Level
from settings import *

class Game():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption('ZeldaGame')

        self.clock = pygame.time.Clock()

        self.level = Level()
        self.level.create_map()

    def update(self):
        self.level.update()

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


if __name__ == '__main__':
    g = Game()
    g.mainloop()
