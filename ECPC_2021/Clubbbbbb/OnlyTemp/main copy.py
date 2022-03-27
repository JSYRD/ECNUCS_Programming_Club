import pygame
from sys import exit
class player(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.frameNumber = 8
        self.frameCounter = 0
        self.RunningCounter = 0
        self.loadImages("./Warrior.jpg", self.frameNumber)
        self.rect = self.frames[0].get_rect()
    def loadImages(self, path, frameNumber):
        sheet = pygame.transform.flip(pygame.image.load(path).convert(),True,False)
        self.frames = []
        for i in range(0,frameNumber):
            tempSurface = pygame.Surface((sheet.get_height(), sheet.get_width()//frameNumber))
            tempSurface.blit(sheet,(0,0),((sheet.get_width()//frameNumber)*i,0,64,64))
            self.frames.append(tempSurface)
    # def rectSetup(self):
    #     self.rect = self.image.get_rect()
    #     self.frameNumber = 8
    #     self.rect.width //= self.frameNumber
    #     self.frameCount = 0
    #     # self.rect.center = (600/2, 400/2)
    #     self.Counter = 0
    def display(self, screen):
        self.RunningCounter += 1
        if self.RunningCounter > 10:
            self.RunningCounter = 0
            self.frameCounter += 1
            self.frameCounter %= self.frameNumber
            self.rect = self.rect.move(10,0)
        screen.blit(self.frames[self.frameCounter],self.rect)


pygame.init()
pygame.display.set_caption("TestOnly")
screen = pygame.display.set_mode((600,400),pygame.SHOWN)
player0 = player(screen)
fclock = pygame.time.Clock()
while True:
    screen.fill(pygame.Color(255,255,255))
    player0.display(screen)
    eventList = pygame.event.get()
    keys = pygame.key.get_pressed()
    for event in eventList:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
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