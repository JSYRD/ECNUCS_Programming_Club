import pygame
from sys import exit
class player(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.flip(pygame.image.load("./Warrior.png"),True,False)
        # self.image.set_colorkey((255,255,255))
        self.rectSetup()
    def rectSetup(self):
        self.rect = self.image.get_rect()
        self.frameNumber = 8
        self.rect.width //= self.frameNumber
        self.frameCount = 0
        # self.rect.center = (600/2, 400/2)
        self.Counter = 0

    def display(self, screen):
        self.Counter += 1
        if self.Counter > 10:
            self.rect.x = self.rect.width*self.frameCount
            self.Counter = 0
            self.frameCount += 1
            self.frameCount %= self.frameNumber
        # self.rect = self.rect.move(10,0)
        screen.blit(self.image,(0,0),self.rect)


pygame.init()
pygame.display.set_caption("TestOnly")
screen = pygame.display.set_mode((600,400),pygame.SHOWN)
player0 = player(screen)
fclock = pygame.time.Clock()
while True:
    screen.fill(pygame.Color(255,255,255))
    eventList = pygame.event.get()
    keys = pygame.key.get_pressed()
    for event in eventList:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
    player0.display(screen)
    pygame.display.flip()
    fclock.tick(60)
















def loadImages(self):
        sheet = pygame.image.load("./Warrior.png")
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