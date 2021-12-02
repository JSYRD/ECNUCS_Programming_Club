import pygame
import data.config as cfg
class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frameNumber = 3
        self.frameIndex = 0
        self.RunningCounter = 0
        self.loadImages("./images/huashileft.png","./images/huashiUp.png","./images/huashiDown.png",3)
        self.image = self.frames[3][0]
        self.rect = self.frames[3][0].get_rect()
        self.rect.center = (100,100)
        self.facingAt = 3
        self.speed = 0
        self.mask = pygame.mask.from_surface(self.frames[0][0])
    def loadImages(self, pathl, pathu, pathd , frameNumber):
        sheetl = pygame.image.load(pathl).convert()
        sheetr = pygame.transform.flip(sheetl,True,False).convert()
        sheetu = pygame.image.load(pathu).convert()
        sheetd = pygame.image.load(pathd).convert()
        # tImage.set_colorkey((255,0,255))
        self.leftFrames = []
        self.rightFrames = []
        self.upFrames = []
        self.downFrames = []
        ratio = 6
        size = (sheetl.get_width()//frameNumber,sheetl.get_height())
        for i in range(0,frameNumber):
            tempSurface = pygame.Surface(size)
            tempSurface.set_colorkey((0,255,0))
            tempSurface.blit(sheetl,(0,0),((sheetl.get_width()//frameNumber)*i,0,size[0],size[1]))
            self.leftFrames.append(pygame.transform.scale(tempSurface.convert(), (size[0]*ratio, size[1]*ratio)))
            tempSurface = pygame.Surface(size)
            tempSurface.set_colorkey((0,255,0))
            tempSurface.blit(sheetr,(0,0),((sheetr.get_width()//frameNumber)*i,0,size[0],size[1]))
            self.rightFrames.append(pygame.transform.scale(tempSurface.convert(), (size[0]*ratio, size[1]*ratio)))
            tempSurface = pygame.Surface(size)
            tempSurface.set_colorkey((0,255,0))
            tempSurface.blit(sheetu,(0,0),((sheetu.get_width()//frameNumber)*i,0,size[0],size[1]))
            self.upFrames.append(pygame.transform.scale(tempSurface.convert(), (size[0]*ratio, size[1]*ratio)))
            tempSurface = pygame.Surface(size)
            tempSurface.set_colorkey((0,255,0))
            tempSurface.blit(sheetd,(0,0),((sheetd.get_width()//frameNumber)*i,0,size[0],size[1]))
            self.downFrames.append(pygame.transform.scale(tempSurface.convert(), (size[0]*ratio, size[1]*ratio)))
        self.frames = [self.upFrames, self.downFrames, self.leftFrames, self.rightFrames]
    def changeCompass(self, compass):
        self.facingAt = compass
    def update(self, keys, screen):
        if keys[pygame.K_RIGHT]:
            self.facingAt = 3
        if keys[pygame.K_LEFT]:
            self.facingAt = 2
        if keys[pygame.K_UP]:
            self.facingAt = 0
        if keys[pygame.K_DOWN]:
            self.facingAt = 1
        self.RunningCounter += 1
        if self.RunningCounter > 10:
            self.RunningCounter = 0
            self.frameIndex += 1
            self.frameIndex %= self.frameNumber
            self.rect = self.rect.move(cfg.COMPASS[self.facingAt][0]*10,cfg.COMPASS[self.facingAt][1]*10)
        self.image = self.frames[self.facingAt][self.frameIndex]
        screen.blit(self.image,self.rect)

