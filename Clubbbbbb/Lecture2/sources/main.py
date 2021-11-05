import os
import pygame
from components import ball,tools
import data.config as cfg
from sys import exit

tools.setup()
screen = pygame.display.set_mode(cfg.SIZE)
myBall = ball.Ball()#create a ball

while(True):
    eventList = pygame.event.get()
    screen.fill(cfg.BG_COLOR)
    
    #create a ball
    sprites = pygame.sprite.Group()
    sprites.add(myBall)


    for event in eventList:
        tools.detectQuit(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            myBall.move(event.pos[0], event.pos[1])
    tools.flash(sprites,screen)