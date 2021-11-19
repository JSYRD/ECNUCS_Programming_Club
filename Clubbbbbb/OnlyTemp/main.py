import pygame
from sys import exit

class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.loadImages()
        Timage = pygame.image.load("./Warrior.png").convert_alpha()
        self.image = pygame.Surface((64, 64))
        self.rect = self.image.blit(Timage, (0, 0), (0,0,64,64))
        self.rect.center = (600/2, 400/2)
    def loadImages(self):
        sheet = pygame.image.load("./Warrior.png").convert_alpha()
        self.frames = []
        self.rightFrames = []
        self.leftFrames = []
        frameRects = [
            (0,0,64,64),
            (64,0,64,64),
            (128,0,64,64),
            (192,0,64,64),
            (256,0,64,64),
            (320,0,64,64),
            (384,0,64,64),
            (448,0,64,64),
        ]
        
        for frameRect in frameRects:
            leftImage = pygame.Surface((64, 64)).blit(sheet, (0, 0), frameRect)
            rightImage = pygame.transform.flip(pygame.Surface((64, 64)).blit(sheet, (0, 0), frameRect),True, False)
            self.rightFrames.append(rightImage)
            self.leftFrames.append(leftImage)
        
        self.frameIndex=0
        self.frames = self.rightFrames
        self.image = self.frames[self.frameIndex]
        self.rect = self.image.get_rect()
    def display(self, screen):
        screen.blit(self.image, self.rect)


pygame.init()
pygame.display.set_caption("TestOnly")
screen = pygame.display.set_mode((600,400),pygame.SHOWN)
player0 = player()
while True:
    screen.fill((255,255,255))
    eventList = pygame.event.get()
    keys = pygame.key.get_pressed()
    for event in eventList:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
    player0.display(screen)
    pygame.display.flip()