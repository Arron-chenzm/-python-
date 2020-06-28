import sys, pygame
from pygame import *
import threading
import time
import os
from Button import Button
from test_res import test_res
from qesandans import qesandans
from PIL import ImageTk, Image
import random

filename = "czm"



pygame.init()
size = width, height = 500, 330
list_time_res = [0] * 12
window = pygame.display.set_mode(size)
surBtnNormal = pygame.image.load("./btn_normal.png").convert_alpha()
surBtnMove = pygame.image.load("./btn_move.png").convert_alpha()
surBtnDown = pygame.image.load("./btn_down.png").convert_alpha()
# 按钮使用的字体
btnFont = pygame.font.SysFont("lisu", 40)
delay_time = 0  # 问卷进行的时间,单位1000/60ms


# 产生1-6的随机数，用于控制刺激帧出现时长
def time_random1():
    num = random.randint(1, 5)
    return num


def time_random2():
    num = random.randint(2, 12)
    return num


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


def strrandom():  # 生成随机算数
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


appear_time = []  # 储存刺激出现的时间
for time_i in range(1, 7):
    appear_time.append(300 * (time_i - 1) + time_random1() * 60 - time_random2())

myfont = pygame.font.SysFont('宋体', 150)
myfont1 = pygame.font.SysFont('宋体', 30)
answer = []  # 储存问题1回答
result = []  # 储存问题1的正确答案
surface = []
question = []  # feiqi问卷问题
answer2 = [0, 0, 0, 0]  # feiqi储存问卷的回答
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
for i in range(1, 62):
    list.append(i * 60)
num = 0
count = 1
t2 = 0
res = 0
t1 = time.time()
while 1:
    while t2 - delay_time < 1000 / 60 * (count + 1):
        t2 = toc(t1)
    count = count + 1
    if count == list[-1]:
        fp = open("{}.txt".format(filename), 'w')  # 如果有这个文件就打开，如果没有这个文件就创建一个名叫CSDN的txt文件
        fp.write(str(list_time_res))
        fp.close()
        print("{}:{}".format("回答正确率", acc(answer, result)))
        for __i in list_time_res:
            print(__i)

        sys.exit()
    for event in pygame.event.get():  # 获取用户当前所做动作的事件列表
        if event.type == pygame.QUIT:
            fp = open("{}.txt".format(filename), 'w')  # 如果有这个文件就打开，如果没有这个文件就创建一个名叫CSDN的txt文件
            fp.write(list_time_res[0])
            fp.close()
            print("{}:{}".format("回答正确率", acc(answer, result)))
            for i in answer2:
                print(i)
            sys.exit()
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if res <= -2:
                if event.key == K_RIGHT:
                    answer2[abs(res) - 2] = 1

                elif event.key == K_LEFT:
                    answer2[abs(res) - 2] = -1
            else:
                if event.key == K_RIGHT:
                    num = num + 1
                    answer.append(1)
                elif event.key == K_LEFT:
                    num = num + 1
                    answer.append(-1)
    # 5秒时进入问卷
    if count in [300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000, 3300, 3600]:
        time_start1 = toc(t1)
        listnum = int(count / 300 - 1)
        #print("time_start1:{}".format(time_start1))
        qesans0 = qesandans(window=window, t1=t1, time_start=time_start1, delay_time=delay_time,
                            list_time_res=list_time_res, list_num=listnum)
        qesans0.run()
        delay_time = qesans0.get_delaytime()
    for i in range(0, len(list)):
        if count == list[i]:
            # 显示背景照片
            window.blit(imagebox[i], (0, 0))
            res = i
            pygame.display.update()
            #print(toc(t1))
            #print(i)

        elif count == appear_time[0]:
            # 显示刺激照片
            window.blit(imagebox2[1], (0, 0))
            res = -1
            pygame.display.update()
            #print(toc(t1))
            #print(count)
            break
        elif count == appear_time[1]:
            # 显示刺激照片2940
            window.blit(imagebox2[2], (0, 0))
            res = -1
            pygame.display.update()
            #print(toc(t1))
            #print(count)
            break
        elif count == appear_time[2]:
            # 显示刺激照片4800
            window.blit(imagebox2[3], (0, 0))
            res = -1
            pygame.display.update()
            #print(toc(t1))
            #print(count)
            break
        elif count == appear_time[3]:
            # 显示刺激照片6480
            window.blit(imagebox2[4], (0, 0))
            res = -1
            pygame.display.update()
            #print(toc(t1))
            #print(count)
            break
        elif count == appear_time[4]:
            # 显示刺激照片6480
            window.blit(imagebox2[5], (0, 0))
            res = -1
            pygame.display.update()
            #print(toc(t1))
            #print(count)
            break
        elif count == appear_time[5]:
            # 显示刺激照片6480
            window.blit(imagebox2[6], (0, 0))
            res = -1
            pygame.display.update()
            #print(toc(t1))
            #print(count)
            break
    if res >= 0:
        window.blit(imagebox[res], (0, 0))
        # 显示背景照片
    if res > -2:
        window.blit(surface[num], (40, 120))
        # 显示问题
    if res <= -2:
        window.fill((0, 0, 0))
        window.blit(question[0], (40, 120))
        # 显示试卷
    pygame.display.update()
