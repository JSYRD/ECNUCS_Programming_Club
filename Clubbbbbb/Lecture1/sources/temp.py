# import pygame
# import os
# SIZE = (1080,720)
# BG_COLOR = (255,255,255)
# class Ball(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.transform.scale(pygame.image.load("./images/ball.png","The ball").convert(),(120,120))
#         self.rect = self.image.get_rect()
#         self.image.set_colorkey(BG_COLOR)
#         self.windowsInfo = pygame.display.Info()
#         self.rect.center = (self.windowsInfo.current_w/2,self.windowsInfo.current_h/2)
#         self.speed = 0
#     def move(self,x,y):
#         self.rect.center = (x,y)

# pygame.init()
# pygame.display.set_caption("Hello World!")
# SCREEN = pygame.display.set_mode(SIZE)
# myBall = Ball()
# while True:
#     SCREEN.fill(BG_COLOR)
#     eventList = pygame.event.get()
#     sprites = pygame.sprite.Group()
#     sprites.add(myBall)
#     for event in eventList:
#         if event.type == pygame.QUIT:
#             exit()
#         elif event.type == pygame.KEYDOWN:
#             if(event.key == pygame.K_ESCAPE):
#                 exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             myBall.move(event.pos[0],event.pos[1])
#     sprites.draw(SCREEN)
#     sprites.update()
#     pygame.display.flip()

class Animal():
    def __init__(self, name):
        self.name = name 
    def eat(self):
        print("Now " +self.name+" is eating.")
class Human(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
    def speak(self, sentence):
        print("Now "+self.name+" is saying: "+sentence)
Dongdong = Human("Dongdong")
Dongdong.speak("I'm not saying anything.")