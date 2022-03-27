#导入必须包
import pygame
from sys import exit

#常量设置
SCREENSIZE = (600,400)#窗口尺寸
BG_COLOR = (255,255,255)

#pygame初始化
pygame.init()
pygame.display.set_caption("Your Caption")
pygame.display.init()

#游戏循环
while True:
    eventList = pygame.event.get()#获得事件
    screen.fill(BG_COLOR)#填充背景
    for event in eventList:#对事件逐一响应
        if(event.type == pygame.QUIT):
            exit()
       #if(Your conditions)...:
       #    do_something()
    pygame.display.flip()