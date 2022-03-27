

## 加环境变量：

![image-20211022230010972](..\image-20211022230010972.png)

![QQ图片20211022230032](..\QQ图片20211022230032.png)

![QQ图片20211022230054](..\QQ图片20211022230054.png)

![QQ图片20211022230058](..\QQ图片20211022230058.png)

![QQ图片20211022230120](..\QQ图片20211022230120.png)

建议把python也加到环境变量里面。

---



## 安装pygame

win+r

![image-20211022230154280](..\image-20211022230154280.png)

输入 按enter

```powershell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pygame
```





## 代码解释

**main.py**:

```python
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
```

前5行是导入包部分。import的具体用法可以自行百度或者CSDN。

第7行使用了tools里的setup方法，如下：

```python
def setup():
    pygame.init()
    pygame.display.set_caption("Hello World!")
```

事实上就是pygame的初始化。



第8行创建了一个窗口SCREEN，尺寸为cfg.SIZE，具体值在data/config.py内：

```python
import pygame
BG_COLOR=pygame.Color(255,255,255)
SIZE = (WIDTH,HEIGHT) = (1080,720)
FPS = 60
g=0.2
```



第9行创建了Ball的对象。

11行-24行是游戏主循环。

第12行是获取pygame事件，是一个列表并赋值给eventList。

第13行是填充SCREEN白色。

16-17行是创建一个sprite的组，并且把myBall加进去。

20-24行是交互循环，主要包含了退出检测tools.detectQuit():

```python
def detectQuit(event):
    if event.type == (pygame.QUIT):
            print("Bye!")
            exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            print("Bye!")
            exit()
```

鼠标检测和刷新tools.flash():

```python
def flash(sprites,screen):
    fclock = pygame.time.Clock()
    sprites.update()
    sprites.draw(screen)
    pygame.display.flip()
    fclock.tick(cfg.FPS)
```

>  这里有一句没有提到的就是fclock，他是一个pygame.time里的Clock对象，主要用于控制游戏帧率。可以用fclock.tick(FPS) 来限制游戏帧率。

