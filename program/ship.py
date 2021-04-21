import pygame

from .functions import getPath
from .life import Life
from .bullets import Bullet

cores = {0: getPath('images\ships\ship_red.png'),
         1: getPath('images\ships\ship_pink.png'),
         2: getPath('images\ships\ship_purple.png'),
         3: getPath('images\ships\ship_blue.png'),
         4: getPath('images\ships\ship_green.png')}

class Ship():
    def __init__(self, screen, color, vel, life):
        self.screen = screen
        self.color = color

        self.image = pygame.image.load(cores[color])

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 50

        self.movingL = False
        self.movingR = False

        self.life = life

        if self.life == 1:
            self.lifes = [Life(screen, self.rect.centerx + 30*n, 780) for n in range(0, life)]
        elif self.life == 3:
            self.lifes = [Life(screen, self.rect.centerx - 29 + 30*n, 780) for n in range(0, life)]
        elif self.life == 5:
            self.lifes = [Life(screen, self.rect.centerx - 59 + 30*n, 780) for n in range(0, life)]

        self.velocity = vel

        self.bullet = Bullet(screen, self.rect.centerx, self.rect.bottom)
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

        for life in self.lifes:
            life.blitme()
    
    def update(self):
        if self.movingL and self.rect.centerx >= 35:
            self.rect.centerx -= self.velocity

            for life in self.lifes:
                life.rect.centerx -= self.velocity
        
        if self.movingR and self.rect.centerx <= 1165:
            self.rect.centerx += self.velocity

            for life in self.lifes:
                life.rect.centerx += self.velocity
    
    def hit(self):
        self.life -= 1

        if self.life % 2 == 0:
            del self.lifes[-1]
        else:
            del self.lifes[0]
