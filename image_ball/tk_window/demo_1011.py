import sys, pygame
from pygame import *
import threading
import time
import os

from PIL import ImageTk, Image

pygame.init()
size = width, height = 500, 330
window = pygame.display.set_mode(size)


def getfiles(Path):
    """获取图片文件名。"""
    files = os.listdir(Path)
    for x in files:
        if not (x.endswith('.jpg') or x.endswith('.JPG') or x.endswith('.png')):
            files.remove(x)
    return files


textlist = ['1', '2', '3', '55', '54', '1', '2', '3', '55', '54', '1', '2', '3', '55', '54', '1', '2', '3', '55', '54',
            '1', '2', '3', '55', '54'
    , '2', '3', '55', '54', '1', '2', '3', '55', '54', '1', '2', '3', '55', '54', '2', '3', '55', '54', '1', '2', '3',
            '55', '54', '1', '2', '3', '55', '45']
myfont = pygame.font.SysFont('宋体', 60)
surface = []
for text in textlist:
    surface.append(myfont.render(text, False, (200, 200, 10)))
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


t = 1000  # 间隔
mt = 1/60*1000*10
t2 = 0
count = 0
t1 = time.time()
for i in range(0, num+count):
    if i - count != 10:
        while t2 < t * i:
            t2 = toc(t1) + count * t
            for event in pygame.event.get():  # 获取用户当前所做动作的事件列表
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    # 检测按键是否是a或者left
                    if event.key == K_LEFT or event.key == K_RIGHT:
                        print('right')
                        t2 = t * i
                        count = count + 1
                        continue
    if i - count == 10:
        while t2 < t * (i - 1) + mt:
            t2 = toc(t1) + count * t
            for event in pygame.event.get():  # 获取用户当前所做动作的事件列表
                if event.type == pygame.QUIT:
                    sys.exit()

    print(i)
    if i - count == 9:
        window.blit(imagebox2[i], (0, 0))
    else:
        if count == 0:
            window.blit(imagebox[i], (0, 0))
        elif count > 0:
            window.blit(imagebox[i - count], (0, 0))

    window.blit(surface[count], (230, 160))
    print(toc(t1))
    pygame.display.update()
