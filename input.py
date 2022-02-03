import pygame


class Input():
    def __init__(self) -> None:
        self.keys = pygame.key.get_pressed()

    def update(self):
        self.keys = pygame.key.get_pressed()

    def left(self) -> bool:
        return self.keys[pygame.K_LEFT]

    def right(self) -> bool:
        return self.keys[pygame.K_RIGHT]

    def up(self) -> bool:
        return self.keys[pygame.K_UP]

    def down(self) -> bool:
        return self.keys[pygame.K_DOWN]
