import pygame
import sys
from settings import *
from player import Player

class Game():
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('myGame')

        self.clock = pygame.time.Clock()

        self.player = Player()

    def update(self):
        self.player.update()

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
