import sys
import pygame
from os.path import join
from pathlib import Path

###################################Processamento##################################

def getPath(path):
    return join(Path.cwd(), path)

######################################Start######################################

def checkEventsInitial(inic, sky):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_w]:
                inic.state = (inic.state - 1) % 2

            if event.key in [pygame.K_DOWN, pygame.K_s]:
                inic.state = (inic.state + 1) % 2
            
            if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                if inic.state == 0:
                    inic.val = 0
                elif inic.state == 1:
                    inic.val = 1
            
            if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                sky.on = True

def updateScreenInitial(sett, screen, sky, inic):
    screen.fill(sett.back)
    sky.blitBack()
    inic.blitInitial()
    
    if inic.state == 0:
        inic.blitStartSelec()
    elif inic.state == 1:
        inic.blitOptionSelec()

    pygame.display.flip()

#####################################Options#####################################

def checkEventsOptions(opt, sky):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_w]:
                opt.state = (opt.state - 1) % 4

            if event.key in [pygame.K_DOWN, pygame.K_s]:
                opt.state = (opt.state + 1) % 4
            
            if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                if opt.state == 0:
                    opt.val = 0
                elif opt.state == 1:
                    opt.val = 1
                elif opt.state == 2:
                    opt.val = 2
                elif opt.state == 3:
                    opt.val = 3
            
            if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                sky.on = True

def updateScreenOptions(sett, screen, sky, opt):
    screen.fill(sett.back)
    sky.blitBack()
    opt.blitOptions()
    
    if opt.state == 0:
        opt.blitShipSelec()
    elif opt.state == 1:
        opt.blitLevelSelec()
    elif opt.state == 2:
        opt.blitControlSelec()
    elif opt.state == 3:
        opt.blitBackSelec()

    pygame.display.flip()

###################################Ship Choose###################################

def checkEventsShips(Ships, sky):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                Ships.color = (Ships.color - 1) % 5
                Ships.dist(0)

            if event.key in [pygame.K_RIGHT, pygame.K_d]:
                Ships.color = (Ships.color + 1) % 5
                Ships.dist(1)
            
            if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                Ships.back = True
            
            if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                sky.on = True

def updateScreenShips(sett, screen, sky, Ships):
    screen.fill(sett.back)
    sky.blitBack()
    Ships.blitBoxes()
    Ships.blitSelec()
    pygame.display.flip()

##################################Level Choose##################################

def checkEventsLevel(level, sky):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_w]:
                level.lel = (level.lel - 1) % 4

            if event.key in [pygame.K_DOWN, pygame.K_s]:
                level.lel = (level.lel + 1) % 4
            
            if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                level.back = True
            
            if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                sky.on = True

def updateScreenLevel(sett, screen, sky, level):
    screen.fill(sett.back)
    sky.blitBack()
    level.blitLevels()
    
    if level.lel == 0:
        level.blitEasySelec()
    elif level.lel == 1:
        level.blitMediumSelec()
    elif level.lel == 2:
        level.blitHardSelec()
    elif level.lel == 3:
        level.blitInsaneSelec()

    pygame.display.flip()

####################################Controls####################################

def checkEventsControls(control, sky):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                control.back = True
            
            if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                sky.on = True

def updateScreenControls(sett, screen, sky, control):
    screen.fill(sett.back)
    sky.blitBack()
    control.blitControls()
    pygame.display.flip()

#####################################Count#####################################

def updateScreenCount(sett, screen, sky, count, num):
    screen.fill(sett.back)
    sky.blitBack()
    count.blitNum(num)
    pygame.display.flip()

######################################Game######################################

def checkEventsLead(screen, ship, sky):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            keydownEventLead(screen, event, ship, sky)
        elif event.type == pygame.KEYUP:
            keyupEventLead(event, ship)

def keydownEventLead(screen, event, ship, sky):
    if event.key in [pygame.K_RIGHT, pygame.K_d]:
        ship.movingR = True
    if event.key in [pygame.K_LEFT, pygame.K_a]:
        ship.movingL = True
    
    if event.key == pygame.K_SPACE:
        ship.bullet.moving = True
    
    if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
        sky.on = True

def keyupEventLead(event, ship):
    if event.key in [pygame.K_RIGHT, pygame.K_d]:
        ship.movingR = False
    if event.key in [pygame.K_LEFT, pygame.K_a]:
        ship.movingL = False

def updateScreenLead(sett, screen, sky, ship, enemie):
    screen.fill(sett.back)
    sky.blitBack()
    ship.bullet.blitme()
    ship.blitme()
    enemie.blitme()
    pygame.display.flip()

def gameover(defeat):
    if defeat:
        return True
    else:
        return False

def updateEnd(sett, screen, sky, end, defeat):
    screen.fill(sett.back)
    sky.blitBack()
    end.blitEnd(defeat)
    pygame.display.flip()
