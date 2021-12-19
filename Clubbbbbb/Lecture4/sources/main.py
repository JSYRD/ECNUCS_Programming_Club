import random
import pygame
from pygame.constants import MOUSEBUTTONDOWN
from components import tools
from components.beast import Beast
import data.config as cfg
from sys import exit

tools.setup()
screen = pygame.display.set_mode(cfg.SIZE,pygame.FULLSCREEN)#surface

backgroundSprites = tools.setupBackground()
warriorGroup = tools.setupWarriorGroup()
beastGroup = tools.setupBeastGroup()
beastIterator = beastGroup.__iter__()
sprites = [backgroundSprites,warriorGroup, beastGroup]

while(True):
    eventList = pygame.event.get()
    # screen.fill((255,255,255))
    keys=pygame.key.get_pressed()
    for event in eventList:
        tools.detectQuit(event)
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            warriorGroup.sprites()[0].changeCompass()
    tools.collidedDetect(warriorGroup,beastGroup)
    # warrior.update(keys,screen)
    if(random.randint(1,100) == 1 and bool(beastGroup)):
        beastGroup.sprites()[random.randint(0,len(beastGroup)-1)].changeCompass()
    tools.flash(screen,keys,sprites)