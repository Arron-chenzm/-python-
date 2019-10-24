import sys, pygame
from pygame import *
import threading
import time
import os
from PIL import ImageTk, Image
import random

pygame.init()
size = width, height = 500, 330
window = pygame.display.set_mode(size)


def strrandom():
    num1 = random.randint(0, 50)
    num2 = random.randint(0, 50)
    p = random.uniform(0, 1)
    if p > 0.5:
        sum = num1 + num2
    else:
        sum = random.randint(50, 100)
    str = "{}+{}={}?".format(num1, num2, sum)
    return str

def getfiles(Path):
    """获取图片文件名。"""
    files = os.listdir(Path)
    for x in files:
        if not (x.endswith('.jpg') or x.endswith('.JPG') or x.endswith('.png')):
            files.remove(x)
    return files



myfont = pygame.font.SysFont('宋体', 150)
surface = []
for i in range(0,100):
    str = strrandom()
    surface.append(myfont.render(str, False, (200, 200, 10)))
    print(str)
imagebox = []
imagebox2 = []
Path = "D:\\Users\\chen\\Desktop\\new\\ciji\\database\\database2\\cat10"
Path2 = "D:\\Users\\chen\\Desktop\\new\\ciji\\database\\database2\\butterfly06"
files = getfiles(Path)
files2 = getfiles(Path2)
num = 50  # 图片数目
for i in range(0, num):
    imagebox.append(pygame.image.load(Path + '\\' + files[i]))
for i in range(0, num - 10):
    imagebox2.append(pygame.image.load(Path2 + '\\' + files2[i]))


def toc(t1):
    t = time.time()
    return (t - t1) * 1000


num = 0
count = 1
t2 = 0
res = 0
t1 = time.time()
# list = [2,62,122,182,242,302,362,422,500,560,620,680,740,800,860,1300]
list = [2]
for i in range(1, 51):
    list.append(60 * i)
while 1:
    while t2 < 1000 / 60 * count:
        t2 = toc(t1)
    count = count + 1
    if count == list[-1]:
        sys.exit()
    for event in pygame.event.get():  # 获取用户当前所做动作的事件列表
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_LEFT or event.key == K_RIGHT:
                print('right')
                num = num + 1
    # print(t2）

    for i in range(0, len(list)):
        if count == list[i]:
            window.blit(imagebox[i], (0, 0))
            res = i

            pygame.display.update()
            print(toc(t1))
            print(i)

        elif count == 476:
            window.blit(imagebox2[0], (0, 0))
            res = -1
            pygame.display.update()
            print(toc(t1))
            print(count)
            break
    if res != -1:
        window.blit(imagebox[res], (0, 0))
    window.blit(surface[num], (40, 120))
    pygame.display.update()
