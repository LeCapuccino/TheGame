import pygame

from .functions import getPath
from .life import Life

cores_pawn = {0: getPath('images\enemies\pawn\pawn_blue.png'),
              1: getPath('images\enemies\pawn\pawn_pink.png'),
              2: getPath('images\enemies\pawn\pawn_yellow.png')}

cores_knight = {0: getPath('images\enemies\knight\knight_blue.png'),
                1: getPath('images\enemies\knight\knight_green.png'),
                2: getPath('images\enemies\knight\knight_red.png'),
                3: getPath('images\enemies\knight\knight_yellow.png')}

cores_pishop = {0: getPath('images\enemies\pishop\pishop_blue.png'),
                1: getPath('images\enemies\pishop\pishop_green.png'),
                2: getPath('images\enemies\pishop\pishop_pink.png'),
                3: getPath('images\enemies\pishop\pishop_purple.png')}

class Pawn():
    def __init__(self, screen, color, posx, vel, life, ship):
        self.screen = screen
        self.color = color

        self.image = pygame.image.load(cores_pawn[color])

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = posx
        self.rect.bottom = 0

        self.life = life

        if self.life == 1:
            self.lifes = [Life(screen, posx, self.rect.bottom - 50)]
        elif self.life == 2:
            self.lifes = [Life(screen, posx - 16, self.rect.bottom - 50),
                          Life(screen, posx + 16, self.rect.bottom - 50)]

        self.velocity = vel
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

        for life in self.lifes:
            life.blitme()
    
    def move(self, vel):
        if self.velocity != -1:
            if vel % self.velocity == 0:
                self.rect.bottom += 1

                for life in self.lifes:
                    life.rect.bottom += 1
        else:
            self.rect.bottom += 2

            for life in self.lifes:
                    life.rect.bottom += 2
    
    def colision(self, ship):
        if ship.bullet.moving:
            if self.rect.centerx - 27 <= ship.bullet.rect.centerx <= self.rect.centerx + 27:
                if ship.bullet.rect.bottom <= self.rect.bottom - 8:
                    self.life -= 1

                    del self.lifes[-1]

                    ship.bullet.moving = False
    
    def invade(self):
        if self.rect.bottom == 800:
            return True
        else:
            return False

    def death(self):
        if self.life <= 0:
            return True
        else:
            return False

class Knight():
    def __init__(self, screen, color, posx, vel, life, ship):
        self.screen = screen
        self.color = color

        self.image = pygame.image.load(cores_knight[color])

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = posx
        self.rect.bottom = 0

        self.life = life

        if self.life == 1:
            self.lifes = [Life(screen, posx, self.rect.bottom - 70)]
        elif self.life == 2:
            self.lifes = [Life(screen, posx - 16, self.rect.bottom - 70),
                          Life(screen, posx + 16, self.rect.bottom - 70)]

        self.velocity = vel
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

        for life in self.lifes:
            life.blitme()
    
    def move(self, vel):
        if self.velocity != -1:
            if vel % self.velocity == 0:
                self.rect.bottom += 1

                for life in self.lifes:
                    life.rect.bottom += 1
        else:
            self.rect.bottom += 2

            for life in self.lifes:
                    life.rect.bottom += 2
    
    def colision(self, ship):
        if ship.bullet.moving:
            if self.rect.centerx - 31 <= ship.bullet.rect.centerx <= self.rect.centerx + 31:
                if ship.bullet.rect.bottom <= self.rect.bottom - 20:
                    self.life -= 1
                    
                    del self.lifes[-1]

                    ship.bullet.moving = False

    def invade(self):
        if self.rect.bottom == 800:
            return True
        else:
            return False

    def death(self):
        if self.life <= 0:
            return True
        else:
            return False

class Pishop():
    def __init__(self, screen, color, posx, vel, life, ship):
        self.screen = screen
        self.color = color

        self.image = pygame.image.load(cores_pishop[color])

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = posx
        self.rect.bottom = 0

        self.life = life

        if self.life == 1:
            self.lifes = [Life(screen, posx, self.rect.bottom - 70)]
        elif self.life == 2:
            self.lifes = [Life(screen, posx - 16, self.rect.bottom - 70),
                          Life(screen, posx + 16, self.rect.bottom - 70)]

        self.velocity = vel

    def blitme(self):
        self.screen.blit(self.image, self.rect)

        for life in self.lifes:
            life.blitme()
    
    def move(self, vel):
        if vel % self.velocity == 0:
            self.rect.bottom += 1

            for life in self.lifes:
                    life.rect.bottom += 1
    
    def colision(self, ship):
        if ship.bullet.moving:
            if self.rect.centerx - 45 <= ship.bullet.rect.centerx <= self.rect.centerx + 45:
                if ship.bullet.rect.bottom <= self.rect.bottom - 12:
                    self.life -= 1

                    del self.lifes[-1]

                    ship.bullet.moving = False

    def invade(self):
        if self.rect.bottom == 800:
            return True
        else:
            return False

    def death(self):
        if self.life <= 0:
            return True
        else:
            return False
