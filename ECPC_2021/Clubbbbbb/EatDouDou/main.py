import pygame
from pygame.constants import K_SPACE
from components import doudou
from components import tools
from components.pacman import Pacman
import data.config as cfg

tools.setup()
screen = pygame.display.set_mode(cfg.SIZE)
pacmanGroup = tools.setupPacman()
sprites = [pacmanGroup]
# backgroundSprites = tools.setupBackground()
FPS = 60
while(True):
    eventList = pygame.event.get()
    screen.fill((0,0,0))
    keys=pygame.key.get_pressed()
    for event in eventList:
        tools.detectQuit(event)
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            FPS = 144 if keys[pygame.K_SPACE] else 60
        if event.type == pygame.KEYUP:
            if(event.key == pygame.K_SPACE) :FPS = 60
            
    #     elif event.type == pygame.MOUSEBUTTONDOWN:
    #         warriorGroup.sprites()[0].changeCompass()
    # tools.collidedDetect(warriorGroup,beastGroup)
    # if(random.randint(1,100) == 1 and bool(beastGroup)):
    #     beastGroup.sprites()[random.randint(0,len(beastGroup)-1)].changeCompass()
    tools.flash(keys, screen, sprites, FPS)