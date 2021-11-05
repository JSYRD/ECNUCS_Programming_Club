import pygame
from data.config import g
from components import tools
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("./images/ball.png","The ball").convert(),(120,120))
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255,255,255))
        self.windowsInfo = pygame.display.Info()
        self.rect.center = (self.windowsInfo.current_w/2,self.windowsInfo.current_h/2)
        self.speed = 0

    def limit(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        if self.rect.left <= 0 :
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0 :
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.speed = (self.speed*-2)/3
    def onGround(self,SCREEN_HEIGHT):
        if self.rect.bottom >SCREEN_HEIGHT:
            return True
        else: 
            return False
    def move(self, posx, posy):
        self.rect.center = (posx, posy)
        self.speed = 0
    def update(self):
        self.limit(self.windowsInfo.current_w, self.windowsInfo.current_h)
        if((abs(self.speed)<0.2)&(self.onGround(self.windowsInfo.current_h-1))):
            self.speed = 0
        else:
            self.rect = self.rect.move([0, self.speed])
            self.speed += g
