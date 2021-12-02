import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('快来打飞机！')
Plane = pygame.image.load('Plane.png')
pygame.display.set_icon(Plane)
bgImg = pygame.image.load('bg.jpg')

pygame.mixer.music.load('bg.mp3')
pygame.mixer.music.play(-1)
bao_sound = pygame.mixer.Sound("jz.mp3")

playerImg = pygame.image.load('wanjia.gif')
PlayerX = 360
PlayerY = 500
PlayerStep = 0

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)


def show_score():
    text = f"Score:{score}"
    score_render = font.render(text, True, (0, 255, 0))
    screen.blit(score_render, (10, 10))

is_over = False
over_font = pygame.font.Font('freesansbold.ttf', 64)
def check_is_over():
    if is_over:
        text = "Game Over"
        render = over_font.render(text, True, (255, 0, 0))
        screen.blit(render, (200, 250))

number_of_enemies = 6

class Enemy():
    def __init__(self):
        self.img = pygame.image.load('enemy.png')
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 250)
        self.step = random.randint(1, 4)


    def reset(self):
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 250)

enemies = []
for i in range(number_of_enemies):
    enemies.append(Enemy())

def distance(bx, by, ex, ey):
    a = bx = ex
    b = by - ey
    return math.sqrt(a*a + b*b)


class Bullet():
    def __init__(self):
        self.img = pygame.image.load('bullet.png')
        self.x = PlayerX + 16
        self.y = PlayerY + 10
        self.step = 10

    def hit(self):
        global score
        for e in enemies:
            if distance(self.x, self.y, e.x, e.y) < 30:
                bao_sound.play()
                bullets.remove(self)
                e.reset()
                score += 1
                print(score)
bullets = []

def show_bullets():
    for b in bullets:
        screen.blit(b.img, (b.x, b.y))
        b.hit()
        b.y -= b.step
        if b.y < 0:
            bullets.remove(b)

def show_enemy():
    global is_over
    for e in enemies:
        screen.blit(e.img, (e.x, e.y))
        e.x += e.step
        if e.x > 735 or e.x < 0:
            e.step *= -1
            e.y += 40
            if e.y > 500:
                is_over = True
                print("游戏结束啦")
                enemies.clear()

def move_player():
    global PlayerX
    PlayerX += PlayerStep
    if PlayerX > 735:
        PlayerX = 735
    if PlayerX < 0:
        PlayerX = 0

running = True
while running:
    screen.blit(bgImg, (0, 0))
    show_score()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                PlayerStep = 0.86
            if event.key == pygame.K_LEFT:
                PlayerStep = -0.86
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet())
        if event.type == pygame.KEYUP:
            PlayerStep = 0

    screen.blit(playerImg, (PlayerX, PlayerY))
    move_player()
    show_enemy()
    show_bullets()
    check_is_over()
    pygame.display.update()
