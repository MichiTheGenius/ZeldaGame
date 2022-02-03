import pygame


class Square():
    def __init__(self, x, y, size, color) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.vel_x = 0
        self.vel_y = 0

    def set_vel_x(self, new_vel_x):
        self.vel_x = new_vel_x

    def set_vel_y(self, new_vel_y):
        self.vel_y = new_vel_y

    def draw(self):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.size, self.size))

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.draw()
