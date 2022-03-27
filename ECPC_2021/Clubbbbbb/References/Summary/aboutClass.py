import pygame
class YourClassName():
    def __init__(self):#必须定义的初始化方法。
       do_something()
   #def Other_methods():
       #.....
#对于pygame的精灵类：
class ClassName(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path)#这里的path是参数，可以是直接写的，也可以是传参数传进来的
        self.rect = self.image.get_rect()