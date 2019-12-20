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


def toc(t1):
    t = time.time()
    return (t - t1) * 1000


def acc(a, b):
    num = len(b) if len(a) > len(b) else len(a)
    sum = 0
    for i in range(0, num):
        if a[i] == b[i]:
            sum = sum + 1
    try:
        return "{:.2%}".format(sum / num)
    except:
        pass


def strrandom():
    num1 = random.randint(0, 50)
    num2 = random.randint(0, 50)
    p = random.uniform(0, 1)
    if p > 0.5:
        sum = num1 + num2
        res = 1
    else:
        sum = random.randint(50, 100)
        res = -1
    str = "{}+{}={}?".format(num1, num2, sum)
    return str, res


def getfiles(Path):
    """获取图片文件名。"""
    files = os.listdir(Path)
    for x in files:
        if not (x.endswith('.jpg') or x.endswith('.JPG') or x.endswith('.png')):
            files.remove(x)
    return files


myfont = pygame.font.SysFont('宋体', 150)
myfont1 = pygame.font.SysFont('宋体', 30)
answer = []  # 储存问题1回答
result = []#储存问题1的正确答案
surface = []
question = []#问卷问题
answer2 = [0,0,0,0]#储存问卷的回答
question.append(myfont1.render("Do you see something else?", False, (200, 200, 10)))
for i in range(0, 300):
    str, res = strrandom()
    surface.append(myfont.render(str, False, (200, 200, 10)))
    result.append(res)
# print(result)
imagebox = []
imagebox2 = []
Path = "D:\\Users\\chen\\Desktop\\new\\ciji\\database\\database2\\cat11"
Path2 = "D:\\Users\\chen\\Desktop\\new\\ciji\\database\\database2\\butterfly06"
files = getfiles(Path)
files2 = getfiles(Path2)
num = 250  # 图片数目
for i in range(0, num):
    imagebox.append(pygame.image.load(Path + '\\' + files[i]))
for i in range(0, 10):
    imagebox2.append(pygame.image.load(Path2 + '\\' + files2[i]))
# list = [2,62,122,182,242,302,362,422,500,560,620,680,740,800,860,1300]
list = []
list.append(1)
for i in range(1,24):
    list.append(i*60)
list.append(1500)
list.append(1800)
for i in range(31,54):
    list.append(i * 60)
list.append(3300)
list.append(3600)
for i in range(61,84):
    list.append(i * 60)
list.append(5100)
list.append(5400)
for i in range(91,114):
    list.append(i * 60)
list.append(6900)
list.append(7200)
num = 0
count = 1
t2 = 0
res = 0
t1 = time.time()
while 1:
    while t2 < 1000 / 60 * (count+1):
        t2 = toc(t1)
    count = count + 1
    if count == list[-1]:
        print("{}:{}".format("回答正确率", acc(answer, result)))
        for i in answer2:
            print(i)

        sys.exit()
    for event in pygame.event.get():  # 获取用户当前所做动作的事件列表
        if event.type == pygame.QUIT:
            print("{}:{}".format("回答正确率", acc(answer, result)))
            for i in answer2:
                print(i)
            sys.exit()
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if res <= -2:
                if event.key == K_RIGHT:
                    answer2[abs(res)-2]=1

                elif event.key == K_LEFT:
                    answer2[abs(res)-2]=-1
            else:
                if event.key == K_RIGHT:
                    num = num + 1
                    answer.append(1)
                elif event.key == K_LEFT:
                    num = num + 1
                    answer.append(-1)
    for i in range(0, len(list)):
        if count == list[i]:#显示背景照片
            window.blit(imagebox[i], (0, 0))
            res = i
            pygame.display.update()
            print(toc(t1))
            print(i)
        elif count == 1500:#显示问卷
            res = -2
            window.fill((0, 0, 0))
        elif count == 3300:#显示问卷
            res = -3
            window.fill((0, 0, 0))
        elif count == 5100:#显示问卷
            res = -4
            window.fill((0, 0, 0))
        elif count == 6900:#显示问卷
            res = -5
            window.fill((0, 0, 0))

        elif count == 714:#显示刺激照片720
            window.blit(imagebox2[1], (0, 0))
            res = -1
            pygame.display.update()
            print(toc(t1))
            print(count)
            break
        elif count == 2900:#显示刺激照片2940
            window.blit(imagebox2[2], (0, 0))
            res = -1
            pygame.display.update()
            print(toc(t1))
            print(count)
            break
        elif count == 4876:#显示刺激照片4800
            window.blit(imagebox2[3], (0, 0))
            res = -1
            pygame.display.update()
            print(toc(t1))
            print(count)
            break
        elif count == 6440:#显示刺激照片6480
            window.blit(imagebox2[4], (0, 0))
            res = -1
            pygame.display.update()
            print(toc(t1))
            print(count)
            break

    if res >=0:
        window.blit(imagebox[res], (0, 0))#显示背景照片
    if res > -2:
        window.blit(surface[num], (40, 120))#显示问题
    if res <= -2:
        window.fill((0, 0, 0))
        window.blit(question[0],(40, 120))#显示试卷
    pygame.display.update()
