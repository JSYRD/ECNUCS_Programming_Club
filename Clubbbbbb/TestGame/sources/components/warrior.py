import pygame
from components import tools
import states.level
class Warrior(pygame.sprite.Sprite):
    def __init__(self, height):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        self.windowsInfo = pygame.display.Info()
        self.rect.center = (100,self.windowsInfo.current_h-height-70)
        self.speed = 2
        self.facingAt = 1


    def loadImages(self):
        # sheet = tools.loadGraphics("./images/Warrior.png")
        sheet = pygame.image.load("./images/Warrior.png").convert_alpha()
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
            leftImage = tools.getImage(sheet, *frameRect, (0,0,0), (64,64))
            rightImage = pygame.transform.flip(tools.getImage(sheet, *frameRect, (0,0,0), (64,64)),True, False)
            self.rightFrames.append(rightImage)
            self.leftFrames.append(leftImage)
        self.frameIndex=0
        self.frames = self.rightFrames
        self.image = self.frames[self.frameIndex]
        self.rect = self.image.get_rect()
        # self.image.set_colorkey((255,255,255))


    def changeCompass(self):
        pass
    def limit(self, center, height):
        if self.rect.left <= 0 :
            self.rect.left = 0
        if self.rect.right > center:
            self.rect.right = center
        if self.rect.top <= 0 :
            self.rect.top = 0
        if self.rect.bottom > self.windowsInfo.current_h-height:
            self.rect.bottom = self.windowsInfo.current_h-height
    def turn(self):
        self.speed = self.speed*-1
    def moveTo(self, posx, posy):
        self.rect.center = (posx, posy)
    def update(self, keys, screen):
        currentTime = pygame.time.get_ticks()
        runningTime = 0
        self.limit(400, 332)
        if keys[pygame.K_RIGHT]:
            self.rect.move(5,0)
            self.frames = self.rightFrames
        if keys[pygame.K_LEFT]:
            self.rect.move(-5,0)
            self.frames = self.leftFrames
        if currentTime > 100:
            runningTime = currentTime
            self.frameIndex += 1
            self.frameIndex %= 4
        self.image = self.frames[self.frameIndex]
        screen.blit(self.image,self.rect)