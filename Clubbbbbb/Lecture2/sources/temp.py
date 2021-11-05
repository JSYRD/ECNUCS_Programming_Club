import pygame
from sys import exit
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__ini
size = (800,400)
pygame.init()
pygame.display.set_caption("Test")
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
BG_Color = (255,255,255)
while True:
    eventList = pygame.event.get()
    screen.fill(BG_Color)
    for event in eventList:
        if(event.type == pygame.QUIT): exit()
    pygame.display.flip()




def add(Name, age):
    return Name+age

print(add(1,2))


print(Name)