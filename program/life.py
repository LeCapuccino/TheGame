import pygame

from .functions import getPath

class Life():
    def __init__(self, screen, x, y):
        self.screen = screen

        self.image = pygame.image.load(getPath('images\life\_life.png'))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = x
        self.rect.bottom = y
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
