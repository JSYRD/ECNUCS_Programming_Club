import pygame
from components import tools
from gameStates import score
class Warrior(pygame.sprite.Sprite):
    def __init__(self, height, path, frameNumber):
        pygame.sprite.Sprite.__init__(self)
        self.frameNumber = frameNumber
        self.frameCounter = 0
        self.RunningCounter = 0
        self.loadImages(path,self.frameNumber)
        self.windowsInfo = pygame.display.Info()
        self.rect = self.frames[1][0].get_rect()
        self.rect.center = (100,self.windowsInfo.current_h-height-70)
        self.speed = 2
        self.facingAt = 1
        self.score = score.Score()
        self.mask = pygame.mask.from_surface(self.frames[1][0])
    def loadImages(self, path, frameNumber):
        tImage = pygame.image.load(path).convert()
        # tImage.set_colorkey((255,0,255))
        # tImage = tImage.convert()
        sheetL = tImage
        sheetR = pygame.transform.flip(tImage,True,False).convert()
        self.frames = [[],[],[]]
        size = (tImage.get_width()//frameNumber,tImage.get_height())
        ratio = 5
        for i in range(0,frameNumber):
            tempSurface = pygame.Surface(size)
            tempSurface.set_colorkey((0,255,0))
            tempSurface.blit(sheetR,(0,0),((sheetR.get_width()//frameNumber)*i,0,size[0],size[1]))
            self.frames[1].append(pygame.transform.scale(tempSurface.convert(), (size[0]*ratio, size[1]*ratio)))

            tempSurface = pygame.Surface(size)
            tempSurface.set_colorkey((0,255,0))
            tempSurface.blit(sheetL,(0,0),((sheetL.get_width()//frameNumber)*i,0,size[0],size[1]))
            self.frames[2].append(pygame.transform.scale(tempSurface.convert(), (size[0]*ratio, size[1]*ratio)))


    def changeCompass(self):
        self.facingAt*=-1
    def limit(self, center, height):
        if self.rect.left <= 0 :
            self.rect.left = 0
        # if self.rect.right > center:
        #     self.rect.right = center
        if self.rect.right > self.windowsInfo.current_w:
            self.rect.right = self.windowsInfo.current_w
        if self.rect.top <= 0 :
            self.rect.top = 0
        if self.rect.bottom > self.windowsInfo.current_h-height:
            self.rect.bottom = self.windowsInfo.current_h-height
    def turn(self):
        self.speed = self.speed*-1
        self.facingAt*=-1
    def moveTo(self, posx, posy):
        self.rect.center = (posx, posy)
    def update(self, screen, keys):
        self.limit(400, 332)
        if keys[pygame.K_RIGHT]:
            self.facingAt = 1
        if keys[pygame.K_LEFT]:
            self.facingAt = -1
        self.RunningCounter += 1
        if self.RunningCounter > 10:
            self.RunningCounter = 0
            self.frameCounter += 1
            self.frameCounter %= self.frameNumber
            self.rect = self.rect.move(10*self.speed*self.facingAt,0)
        self.score.update(screen, keys)
        screen.blit(self.frames[self.facingAt][self.frameCounter],self.rect)
