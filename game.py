import pygame, sys
from settings import *

class Game():
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('myGame')

        self.clock = pygame.time.Clock()

    def mainloop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(BLACK)

            pygame.display.update()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

g = Game()

g.mainloop()