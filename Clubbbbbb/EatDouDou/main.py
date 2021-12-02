import pygame
from components import doudou
from components import tools
from components.pacman import Pacman
import data.config as cfg

tools.setup()
screen = pygame.display.set_mode(cfg.SIZE)
pacmanGroup = tools.setupPacman()
sprites = [pacmanGroup]

# backgroundSprites = tools.setupBackground()
while(True):
    eventList = pygame.event.get()
    screen.fill((0,0,0))
    keys=pygame.key.get_pressed()
    for event in eventList:
        tools.detectQuit(event)
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
    #     elif event.type == pygame.MOUSEBUTTONDOWN:
    #         warriorGroup.sprites()[0].changeCompass()
    # tools.collidedDetect(warriorGroup,beastGroup)
    # if(random.randint(1,100) == 1 and bool(beastGroup)):
    #     beastGroup.sprites()[random.randint(0,len(beastGroup)-1)].changeCompass()
    tools.flash(keys, screen, sprites)