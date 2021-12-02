import pygame
import os

from pygame.sprite import Group, collide_mask#import pygame和os
DEFAULTSIZE = (1080,720)
BG_COLOR = (255,255,255)#常量设置
class Ball(pygame.sprite.Sprite):#Ball类的定义
    def __init__(self):#初始化方法的定义
        pygame.sprite.Sprite.__init__(self)#初始化Sprite
        self.image = pygame.transform.scale(pygame.image.load("./images/ball.png","The ball").convert(),(120,120))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BG_COLOR)
        self.windowsInfo = pygame.display.Info()
        self.rect.center = (self.windowsInfo.current_w/2,self.windowsInfo.current_h/2)
        self.speedX = 0
        self.speedY = 0#对象的初始属性
        self.mask = pygame.mask.from_surface(self.image)
    def move(self,x,y):#移动
        self.speedY=0#让球停下来
        self.rect.center = (x,y)#移动到x,y
    def run(self, compassX, compassY):#让球跑
        self.rect = self.rect.move(compassX*10, compassY*10)#compassX\Y代表方向，*10是每次移动的距离
    def draw(self):
        SCREEN.blit(self.image, self.rect)#在SCREEN上画出球
    def limit(self):#限制球的运动
        if(self.rect.bottom >= self.windowsInfo.current_h):
            self.rect.bottom = self.windowsInfo.current_h
            self.speedY = (-2/3)*self.speedY#反弹
    def update(self):#更新球
        g=0.1#模拟重力加速度
        self.windowsInfo = pygame.display.Info()#实时获取窗口大小信息
        self.speedY +=g#加速加速
        self.rect = self.rect.move(self.speedX, self.speedY)#运动
        self.limit()
        self.draw()


pygame.init()
pygame.display.set_caption("Hello World!")
SCREEN = pygame.display.set_mode(DEFAULTSIZE,pygame.RESIZABLE)#初始化三板斧
fclock = pygame.time.Clock()#时钟
ballGroup = pygame.sprite.Group()
ballGroup.add(Ball())
ballList = ballGroup.sprites()
myBall = Ball()
while True:#游戏主循环
    SCREEN.fill(BG_COLOR)
    eventList = pygame.event.get()
    for event in eventList:#事件检测
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_ESCAPE):
                exit()
            # if(event.key == pygame.K_RIGHT):
            #     myBalls[0].run(1, 0)
            # if(event.key == pygame.K_LEFT):
            #     myBalls[0].run(-1, 0)
            # if(event.key == pygame.K_UP):
            #     myBalls[0].run(0, -1)
            # if(event.key == pygame.K_DOWN):
            #     myBalls[0].run(0, 1)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ballList[0].move(event.pos[0],event.pos[1])
            # for ball in iter(ballGroup):
            #     myBalls[0].move(event.pos[0],event.pos[1])
    # for ball in myBalls:#让所有球都更新
        ballGroup.update()
        myBall.update()
    print(pygame.sprite.spritecollideany(myBall, ballGroup))
    fclock.tick(60)#限定时钟速度
    pygame.display.flip()#更新屏幕