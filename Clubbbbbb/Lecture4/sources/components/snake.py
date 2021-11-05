import pygame
from components import tools
from data.config import standardSize
right = (0,1)
left = (0,-1)
up = (-1,0)
down = (1,0)

class snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.direction = right
        self.snakeList = [head(),body()]
    def forward(self):
        self.snakeList.pop()
        self.snakeList[0].pos = ()
    class head():
        def __init__(self):
            self.image = pygame.transform.scale(pygame.image.load("images/head.png").convert(),standardSize)
            self.windowsInfo = pygame.display.Info()
            self.pos = (self.windowsInfo[0], self.windowsInfo[1])
    class body():
        def __init__(self):
            self.image = pygame.transform.scale(pygame.image.load("images/body.png").convert(),standardSize)
            self.pos = ()