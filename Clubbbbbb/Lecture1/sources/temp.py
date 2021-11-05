import pygame
import os
SIZE = (1080,720)
BG_COLOR = (255,255,255)
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("./images/ball.png","The ball").convert(),(120,120))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BG_COLOR)
        self.windowsInfo = pygame.display.Info()
        self.rect.center = (self.windowsInfo.current_w/2,self.windowsInfo.current_h/2)
        self.speedX = 0
        self.speedY = 0
    def move(self,x,y):
        self.speedY=0
        self.rect.center = (x,y)
    def run(self, compassX, compassY):
        self.rect = self.rect.move(compassX*10, compassY*10)
    def draw(self):
        SCREEN.blit(self.image, self.rect)
    def limit(self):
        if(self.rect.bottom >= self.windowsInfo.current_h):
            self.rect.bottom = self.windowsInfo.current_h
            self.speedY = (-2/3)*self.speedY
    def update(self):
        g=0.1
        self.windowsInfo = pygame.display.Info()
        self.speedY +=g
        self.rect = self.rect.move(self.speedX, self.speedY)
        self.limit()
        self.draw()


pygame.init()
pygame.display.set_caption("Hello World!")
SCREEN = pygame.display.set_mode(SIZE,pygame.RESIZABLE)
myBalls = []
for i in range(2):
    myBalls.append(Ball())
fclock = pygame.time.Clock()

while True:
    SCREEN.fill(BG_COLOR)
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            for ball in myBalls:
                ball.detect(key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            myBalls[0].move(event.pos[0],event.pos[1])
    for ball in myBalls:
        ball.update()
    fclock.tick(60)
    pygame.display.flip()




# class Animal():
#     def __init__(self, name):
#         self.name = name 
#         print("now a new Animal is created.")
#     def eat(self):
#         print("Now " +self.name+" is eating.")

# animal = Animal("Lalala")






# class Human(Animal):
#     def __init__(self, name):
#         Animal.__init__(self, name)
#     def speak(self, sentence):
#         print("Now "+self.name+" is saying: "+sentence)
# Dongdong = Human("Dongdong")
# Dongdong.speak("I'm not saying anything.")




def add(a,b):
    return a+b