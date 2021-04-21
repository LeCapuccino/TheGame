import pygame

from .functions import getPath

class Bullet():
    def __init__(self, screen, center, bottom):
        self.screen = screen

        self.image = pygame.image.load(getPath('images\munition\_bullet.png'))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = center
        self.rect.bottom = bottom

        self.moving = False

        self.velocity = 1
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def update(self, center, bottom):
        if self.moving:
            self.rect.bottom -= self.velocity
        else:
            self.rect.centerx = center
            self.rect.bottom = bottom - 72
        
        if self.rect.bottom <= 0:
            self.moving = False
