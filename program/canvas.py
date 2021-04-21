import pygame

from .functions import getPath

class Background():
    def __init__(self, screen):
        self.screen = screen

        self.back = pygame.image.load(getPath('images\sky\sky.png'))

        self.rect_back = self.back.get_rect()
        self.screen_back = self.screen.get_rect()

        self.rect_back.centerx = 600
        self.rect_back.bottom = 800

        self.on = False
    
    def blitBack(self):
        self.screen.blit(self.back, self.rect_back)

class Initial():
    def __init__(self, screen):
        self.screen = screen

        self.initial = pygame.image.load(getPath('images\elements\_initial\_initial.png'))
        self.start_selec = pygame.image.load(getPath('images\elements\_initial\_startselec.png'))
        self.option_selec = pygame.image.load(getPath('images\elements\_initial\_optionselec.png'))

        self.rect_initial = self.initial.get_rect()
        self.rect_start_selec = self.start_selec.get_rect()
        self.rect_option_selec = self.option_selec.get_rect()

        self.screen_rect_initial = self.screen.get_rect()
        self.screen_rect_start_selec = self.screen.get_rect()
        self.screen_rect_option_selec = self.screen.get_rect()

        self.rect_initial.centerx = 600
        self.rect_start_selec.centerx = 592
        self.rect_option_selec.centerx = 600

        self.rect_initial.bottom = 645
        self.rect_start_selec.bottom = 569
        self.rect_option_selec.bottom = 637

        self.state = 0
        self.val = -1
    
    def blitInitial(self):
        self.screen.blit(self.initial, self.rect_initial)
    
    def blitStartSelec(self):
        self.screen.blit(self.start_selec, self.rect_start_selec)
    
    def blitOptionSelec(self):
        self.screen.blit(self.option_selec, self.rect_option_selec)

class Options():
    def __init__(self, screen):
        self.screen = screen

        self.opt = pygame.image.load(getPath('images\elements\_options\_opt.png'))
        self.ships_selec = pygame.image.load(getPath('images\elements\_options\_ships_selec.png'))
        self.level_selec = pygame.image.load(getPath('images\elements\_options\_level_selec.png'))
        self.controls_selec = pygame.image.load(getPath('images\elements\_options\_controls_selec.png'))
        self.back_selec = pygame.image.load(getPath('images\elements\_options\_back_selec.png'))

        self.rect_opt = self.opt.get_rect()
        self.rect_ships_selec = self.ships_selec.get_rect()
        self.rect_level_selec = self.level_selec.get_rect()
        self.rect_controls_selec = self.controls_selec.get_rect()
        self.rect_back_selec = self.back_selec.get_rect()

        self.screen_opt = self.screen.get_rect()
        self.screen_ships_selec = self.screen.get_rect()
        self.screen_level_selec = self.screen.get_rect()
        self.screen_controls_selec = self.screen.get_rect()
        self.screen_back_selec = self.screen.get_rect()

        self.rect_opt.centerx = 600
        self.rect_ships_selec.centerx = 600
        self.rect_level_selec.centerx = 600
        self.rect_controls_selec.centerx = 600
        self.rect_back_selec.centerx = 600

        self.rect_opt.bottom = 660
        self.rect_ships_selec.bottom = 246
        self.rect_level_selec.bottom = 330
        self.rect_controls_selec.bottom = 414
        self.rect_back_selec.bottom = 652

        self.state = 0
        self.val = -1
    
    def blitOptions(self):
        self.screen.blit(self.opt, self.rect_opt)
    
    def blitShipSelec(self):
        self.screen.blit(self.ships_selec, self.rect_ships_selec)
    
    def blitLevelSelec(self):
        self.screen.blit(self.level_selec, self.rect_level_selec)

    def blitControlSelec(self):
        self.screen.blit(self.controls_selec, self.rect_controls_selec)
    
    def blitBackSelec(self):
        self.screen.blit(self.back_selec, self.rect_back_selec)

class Ships():
    def __init__(self, screen):
        self.screen = screen

        self.boxes = pygame.image.load(getPath('images\elements\_options\_ships\_boxes.png'))
        self.selec = pygame.image.load(getPath('images\elements\_options\_ships\_selec.png'))

        self.rect_boxes = self.boxes.get_rect()
        self.rect_selec = self.selec.get_rect()

        self.screen_rect_boxes = self.screen.get_rect()
        self.screen_rect_selec = self.screen.get_rect()

        self.rect_boxes.centerx = 600
        self.rect_selec.centerx = 352

        self.rect_boxes.bottom = 462
        self.rect_selec.bottom = 462

        self.color = 0
        self.back = False
    
    def blitBoxes(self):
        self.screen.blit(self.boxes, self.rect_boxes)
    
    def blitSelec(self):
        self.screen.blit(self.selec, self.rect_selec)
    
    def dist(self, num): # 352 476 600 724 848
        right = {352: 476, 476: 600, 600: 724, 724: 848, 848: 352}
        left = {352: 848, 476: 352, 600: 476, 724: 600, 848: 724}

        if num == 0:
            self.rect_selec.centerx = left[self.rect_selec.centerx]
        if num == 1:
            self.rect_selec.centerx = right[self.rect_selec.centerx]

class Level():
    def __init__(self, screen):
        self.screen = screen

        self.levels = pygame.image.load(getPath('images\elements\_options\_level\_levels.png'))
        self.easy_selec = pygame.image.load(getPath('images\elements\_options\_level\_easy_selec.png'))
        self.medium_selec = pygame.image.load(getPath('images\elements\_options\_level\_medium_selec.png'))
        self.hard_selec = pygame.image.load(getPath('images\elements\_options\_level\_hard_selec.png'))
        self.insane_selec = pygame.image.load(getPath('images\elements\_options\_level\_insane_selec.png'))

        self.rect_levels = self.levels.get_rect()
        self.rect_easy_selec = self.easy_selec.get_rect()
        self.rect_medium_selec = self.medium_selec.get_rect()
        self.rect_hard_selec = self.hard_selec.get_rect()
        self.rect_insane_selec = self.insane_selec.get_rect()

        self.screen_opt = self.screen.get_rect()
        self.screen_easy_selec = self.screen.get_rect()
        self.screen_medium_selec = self.screen.get_rect()
        self.screen_hard_selec = self.screen.get_rect()
        self.screen_insane_selec = self.screen.get_rect()

        self.rect_levels.centerx = 600
        self.rect_easy_selec.centerx = 600
        self.rect_medium_selec.centerx = 600
        self.rect_hard_selec.centerx = 600
        self.rect_insane_selec.centerx = 600

        self.rect_levels.bottom = 550
        self.rect_easy_selec.bottom = 290
        self.rect_medium_selec.bottom = 372
        self.rect_hard_selec.bottom = 460
        self.rect_insane_selec.bottom = 542
    
        self.lel = 0
        self.back = False

    def blitLevels(self):
        self.screen.blit(self.levels, self.rect_levels)
    
    def blitEasySelec(self):
        self.screen.blit(self.easy_selec, self.rect_easy_selec)
    
    def blitMediumSelec(self):
        self.screen.blit(self.medium_selec, self.rect_medium_selec)

    def blitHardSelec(self):
        self.screen.blit(self.hard_selec, self.rect_hard_selec)
    
    def blitInsaneSelec(self):
        self.screen.blit(self.insane_selec, self.rect_insane_selec)

class Controls():
    def __init__(self, screen):
        self.screen = screen

        self.cont = pygame.image.load(getPath('images\elements\_options\_controls\_controls.png'))

        self.rect_cont = self.cont.get_rect()
        self.screen_cont = self.screen.get_rect()

        self.rect_cont.centerx = 600
        self.rect_cont.bottom = 660

        self.back = False
    
    def blitControls(self):
        self.screen.blit(self.cont, self.rect_cont)

class Count():
    def __init__(self, screen):
        self.screen = screen

        self.num_1 = pygame.image.load(getPath('images\elements\_start\_num_1.png'))
        self.num_2 = pygame.image.load(getPath('images\elements\_start\_num_2.png'))
        self.num_3 = pygame.image.load(getPath('images\elements\_start\_num_3.png'))

        self.rect_num_1 = self.num_1.get_rect()
        self.rect_num_2 = self.num_2.get_rect()
        self.rect_num_3 = self.num_3.get_rect()

        self.screen_num_1 = self.screen.get_rect()
        self.screen_num_2 = self.screen.get_rect()
        self.screen_num_3 = self.screen.get_rect()

        self.rect_num_1.centerx = 600
        self.rect_num_2.centerx = 600
        self.rect_num_3.centerx = 600

        self.rect_num_1.bottom = 500
        self.rect_num_2.bottom = 500
        self.rect_num_3.bottom = 500
    
    def blitNum(self, num):
        if num == 1:
            self.screen.blit(self.num_1, self.rect_num_1)
        elif num == 2:
            self.screen.blit(self.num_2, self.rect_num_2)
        elif num == 3:
            self.screen.blit(self.num_3, self.rect_num_3)

class End():
    def __init__(self, screen):
        self.screen = screen

        self.gameover = pygame.image.load(getPath('images\elements\_final\_gameover.png'))
        self.victory = pygame.image.load(getPath('images\elements\_final\_victory.png'))

        self.rect_gameover = self.gameover.get_rect()
        self.rect_victory = self.victory.get_rect()

        self.screen_gameover = self.screen.get_rect()
        self.screen_victory = self.screen.get_rect()

        self.rect_gameover.centerx = 600
        self.rect_victory.centerx = 600

        self.rect_gameover.bottom = 525
        self.rect_victory.bottom = 456

    def blitEnd(self, defeat):
        if defeat:
            self.screen.blit(self.gameover, self.rect_gameover)
        else:
            self.screen.blit(self.victory, self.rect_victory)
