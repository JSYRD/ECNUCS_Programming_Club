import pygame
from components import tools
import states.level
class Warrior(pygame.sprite.Sprite):
    def __init__(self, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./images/warrior.gif","The ball")
        self.rect = self.image.get_rect()
        # self.image.set_colorkey((255,255,255))
        self.windowsInfo = pygame.display.Info()
        self.rect.center = (100,self.windowsInfo.current_h-height-70)
        self.speed = 2
        self.facingAt = 1
    def loadImages(self):
        sheet = tools.loadGraphics("./images/Warrior.png")
        self.frames = []
        self.rightFrames = []
        self.leftFrames = []
        frameRects = [
            (0,0,64,64),
            (64,0,64,64),
            (128,0,64,64),
            (192,0,64,64),
        ]
        
        for frameRect in frameRects:
            leftImage = tools.get_image(sheet, *frameRect, (0,0,0), (64,64))
            rightImage = pygame.transform.flip(tools.getImage(sheet, *frameRect, (0,0,0), (64,64)),True, False)
            self.rightFrames.append(rightImage)
            self.leftFrames.append(leftImaeg)

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
    def move(self, posx, posy):
        self.rect.center = (posx, posy)
    def update(self, keys):
        self.limit(400, 332)
        self.rect = self.rect.move(self.speed, 0)