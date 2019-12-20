import sys, pygame
from pygame import *
import threading
import time
import os
from Button import Button
from test_res import test_res
from PIL import ImageTk, Image
import random

pygame.init()
size = width, height = 500, 330
window = pygame.display.set_mode(size)
surBtnNormal = pygame.image.load("./btn_normal.png").convert_alpha()
surBtnMove = pygame.image.load("./btn_move.png").convert_alpha()
surBtnDown = pygame.image.load("./btn_down.png").convert_alpha()

list_time_res = [0]*12
# 按钮使用的字体
btnFont = pygame.font.SysFont("lisu", 40)
delay_time = 0  # 问卷进行的时间,单位1000/60ms
def btnCallBack8(): # 开始下一个trail的按钮
    global state
    global delay_time
    state = False
    time_end1 = toc(t1)
    delay_time = delay_time + time_end1 - time_start1
    print(time_start1, time_end1, delay_time)
    print("我被按下了")
    # print(state)
def btnCallBack1():
    print(11)
    pass
def btnCallBack2():
    print(12)
    return 'n'
def btnCallBack3():
    print(13)
    return 'butterfly'
def btnCallBack4():
    print(14)
    return 'dog'
def btnCallBack5():
    print(15)
    return "apple"
def btnCallBack6():
    print(16)
    return "monkey"
def btnCallBack7():
    print(17)
    return "uncertain"

#产生1-6的随机数，用于控制刺激帧出现时长
def time_random1():
    num = random.randint(1,5)
    return num

def time_random2():
    num = random.randint(1,6)
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

appear_time = []  # 储存刺激出现的时间
for time_i in range(1,7):
    appear_time.append(300*(time_i-1)+time_random1()*60-time_random2())

myfont = pygame.font.SysFont('宋体', 150)
myfont1 = pygame.font.SysFont('宋体', 30)
answer = []  # 储存问题1回答
result = []  # 储存问题1的正确答案
surface = []
question = []  # feiqi问卷问题
answer2 = [0,0,0,0]  # feiqi储存问卷的回答
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
for i in range(1,61):
    list.append(i*60)
num = 0
count = 1
t2 = 0
res = 0
t1 = time.time()
while 1:
    while t2-delay_time < 1000 / 60 * (count+1):
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
    # 5秒时进入问卷
    if count== 300:
        time_start1 = toc(t1)
        print(time_start1)

        state = True  # 点击下一个按钮，按钮弹起调用回调函数，会改变state为False，跳出循环。
        btn8 = Button(400, 275, "NEXT", surBtnNormal, surBtnMove, surBtnDown, btnCallBack8, btnFont, (255, 0, 0))
        btn1 = Button(0, 0, "看到", surBtnNormal, surBtnMove, surBtnDown,btnCallBack1,  btnFont, (255, 0, 0))
        btn2 = Button(200, 0, "未看到", surBtnNormal, surBtnMove, surBtnDown, btnCallBack2, btnFont, (255, 0, 0))
        btn3 = Button(0, 100, "蝴蝶", surBtnNormal, surBtnMove, surBtnDown, btnCallBack3, btnFont, (255, 0, 0))
        btn4 = Button(125, 100, "狗", surBtnNormal, surBtnMove, surBtnDown, btnCallBack4, btnFont, (255, 0, 0))
        btn5 = Button(250, 100, "苹果", surBtnNormal, surBtnMove, surBtnDown, btnCallBack5, btnFont, (255, 0, 0))
        btn6 = Button(375, 100, "猴子", surBtnNormal, surBtnMove, surBtnDown, btnCallBack6, btnFont, (255, 0, 0))
        btn7 = Button(100, 200, "不确定", surBtnNormal, surBtnMove, surBtnDown, btnCallBack7, btnFont, (255, 0, 0))
        tr1 = test_res()
        tr1.set_times(1)
        # if (tr1.get_see() == None) & (btnCallBack1() != None):
        #     tr1.set_see(btnCallBack1())
        # if (tr1.get_see() == None) & (btnCallBack2() != None):
        #     tr1.set_see(btnCallBack2())
        # if (tr1.get_thing() == None) & (btnCallBack3() != None):
        #     tr1.set_thing(btnCallBack3())
        # if (tr1.get_thing() == None) & (btnCallBack4() != None):
        #     tr1.set_thing(btnCallBack4())
        # if (tr1.get_thing() == None) & (btnCallBack5() != None):
        #     tr1.set_thing(btnCallBack5())
        # if (tr1.get_thing() == None) & (btnCallBack6() != None):
        #     tr1.set_thing(btnCallBack6())
        # if (tr1.get_thing() == None) & (btnCallBack7() != None):
        #     tr1.set_thing(btnCallBack7())
        while state:
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEMOTION:  # 鼠标移动事件
                    # 判断鼠标是否移动到按钮范围内
                    btn1.getFocus(mx, my)
                    btn2.getFocus(mx, my)
                    btn3.getFocus(mx, my)
                    btn4.getFocus(mx, my)
                    btn5.getFocus(mx, my)
                    btn6.getFocus(mx, my)
                    btn7.getFocus(mx, my)
                    btn8.getFocus(mx, my)
                elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标按下
                    if pygame.mouse.get_pressed() == (1, 0, 0):  # 鼠标左键按下
                        btn1.mouseDown(mx, my)
                        btn2.mouseDown(mx, my)
                        btn3.mouseDown(mx, my)
                        btn4.mouseDown(mx, my)
                        btn5.mouseDown(mx, my)
                        btn6.mouseDown(mx, my)
                        btn7.mouseDown(mx, my)
                        btn8.mouseDown(mx, my)
                        #print("鼠标按下")
                elif event.type == pygame.MOUSEBUTTONUP:  # 鼠标弹起
                    if (tr1.get_see() == None):
                        tr1.set_see(btn1.mouseUp())
                    if (tr1.get_see() == None):
                        tr1.set_see(btn2.mouseUp())
                    if (tr1.get_thing() == None):
                        tr1.set_thing(btn3.mouseUp())
                    if (tr1.get_thing() == None):
                        tr1.set_thing(btn4.mouseUp())
                    if (tr1.get_thing() == None):
                        tr1.set_thing(btn5.mouseUp())
                    if (tr1.get_thing() == None):
                        tr1.set_thing(btn6.mouseUp())
                    if (tr1.get_thing() == None):
                        tr1.set_thing(btn7.mouseUp())
                    btn8.mouseUp2()
                    tr1.printres()
                    list_time_res[0]=tr1.res2str()
                    print(list_time_res[0])
                    print("鼠标弹起")

            # pygame.time.delay(16)
            window.fill((0, 0, 0))
            # 绘制按钮
            btn1.draw(window)
            btn2.draw(window)
            btn3.draw(window)
            btn4.draw(window)
            btn5.draw(window)
            btn6.draw(window)
            btn7.draw(window)
            btn8.draw(window)
            pygame.display.flip()
    # 10秒时进入问卷
    if count== 600:
        time_start2 = toc(t1)
        print(time_start2)

        state = True  # 点击下一个按钮，按钮弹起调用回调函数，会改变state为False，跳出循环。
        btn8 = Button(400, 275, "NEXT", surBtnNormal, surBtnMove, surBtnDown, btnCallBack8, btnFont, (255, 0, 0))
        btn1 = Button(0, 0, "看到", surBtnNormal, surBtnMove, surBtnDown,btnCallBack1,  btnFont, (255, 0, 0))
        btn2 = Button(200, 0, "未看到", surBtnNormal, surBtnMove, surBtnDown, btnCallBack2, btnFont, (255, 0, 0))
        btn3 = Button(0, 100, "蝴蝶", surBtnNormal, surBtnMove, surBtnDown, btnCallBack3, btnFont, (255, 0, 0))
        btn4 = Button(125, 100, "狗", surBtnNormal, surBtnMove, surBtnDown, btnCallBack4, btnFont, (255, 0, 0))
        btn5 = Button(250, 100, "苹果", surBtnNormal, surBtnMove, surBtnDown, btnCallBack5, btnFont, (255, 0, 0))
        btn6 = Button(375, 100, "猴子", surBtnNormal, surBtnMove, surBtnDown, btnCallBack6, btnFont, (255, 0, 0))
        btn7 = Button(100, 200, "不确定", surBtnNormal, surBtnMove, surBtnDown, btnCallBack7, btnFont, (255, 0, 0))
        tr2 = test_res()
        tr2.set_times(2)
        # if (tr1.get_see() == None) & (btnCallBack1() != None):
        #     tr1.set_see(btnCallBack1())
        # if (tr1.get_see() == None) & (btnCallBack2() != None):
        #     tr1.set_see(btnCallBack2())
        # if (tr1.get_thing() == None) & (btnCallBack3() != None):
        #     tr1.set_thing(btnCallBack3())
        # if (tr1.get_thing() == None) & (btnCallBack4() != None):
        #     tr1.set_thing(btnCallBack4())
        # if (tr1.get_thing() == None) & (btnCallBack5() != None):
        #     tr1.set_thing(btnCallBack5())
        # if (tr1.get_thing() == None) & (btnCallBack6() != None):
        #     tr1.set_thing(btnCallBack6())
        # if (tr1.get_thing() == None) & (btnCallBack7() != None):
        #     tr1.set_thing(btnCallBack7())
        while state:
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEMOTION:  # 鼠标移动事件
                    # 判断鼠标是否移动到按钮范围内
                    btn1.getFocus(mx, my)
                    btn2.getFocus(mx, my)
                    btn3.getFocus(mx, my)
                    btn4.getFocus(mx, my)
                    btn5.getFocus(mx, my)
                    btn6.getFocus(mx, my)
                    btn7.getFocus(mx, my)
                    btn8.getFocus(mx, my)
                elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标按下
                    if pygame.mouse.get_pressed() == (1, 0, 0):  # 鼠标左键按下
                        btn1.mouseDown(mx, my)
                        btn2.mouseDown(mx, my)
                        btn3.mouseDown(mx, my)
                        btn4.mouseDown(mx, my)
                        btn5.mouseDown(mx, my)
                        btn6.mouseDown(mx, my)
                        btn7.mouseDown(mx, my)
                        btn8.mouseDown(mx, my)
                        #print("鼠标按下")
                elif event.type == pygame.MOUSEBUTTONUP:  # 鼠标弹起
                    if (tr2.get_see() == None):
                        tr2.set_see(btn1.mouseUp())
                    if (tr2.get_see() == None):
                        tr2.set_see(btn2.mouseUp())
                    if (tr2.get_thing() == None):
                        tr2.set_thing(btn3.mouseUp())
                    if (tr2.get_thing() == None):
                        tr2.set_thing(btn4.mouseUp())
                    if (tr2.get_thing() == None):
                        tr2.set_thing(btn5.mouseUp())
                    if (tr2.get_thing() == None):
                        tr2.set_thing(btn6.mouseUp())
                    if (tr2.get_thing() == None):
                        tr2.set_thing(btn7.mouseUp())
                    btn8.mouseUp2()
                    tr2.printres()
                    list_time_res[1]=tr2.res2str()
                    print(list_time_res[1])
                    print("鼠标弹起")

            # pygame.time.delay(16)
            window.fill((0, 0, 0))
            # 绘制按钮
            btn1.draw(window)
            btn2.draw(window)
            btn3.draw(window)
            btn4.draw(window)
            btn5.draw(window)
            btn6.draw(window)
            btn7.draw(window)
            btn8.draw(window)
            pygame.display.flip()
    for i in range(0, len(list)):
        if count == list[i]:
            # 显示背景照片
            window.blit(imagebox[i], (0, 0))
            res = i
            pygame.display.update()
            print(toc(t1))
            print(i)

        elif count == appear_time[0]:
            # 显示刺激照片
            window.blit(imagebox2[1], (0, 0))
            res = -1
            pygame.display.update()
            print(toc(t1))
            print(count)
            break
        elif count == appear_time[1]:
            # 显示刺激照片2940
            window.blit(imagebox2[2], (0, 0))
            res = -1
            pygame.display.update()
            print(toc(t1))
            print(count)
            break
        elif count == appear_time[2]:
            # 显示刺激照片4800
            window.blit(imagebox2[3], (0, 0))
            res = -1
            pygame.display.update()
            print(toc(t1))
            print(count)
            break
        elif count == appear_time[3]:
            # 显示刺激照片6480
            window.blit(imagebox2[4], (0, 0))
            res = -1
            pygame.display.update()
            print(toc(t1))
            print(count)
            break
        elif count == appear_time[4]:
            # 显示刺激照片6480
            window.blit(imagebox2[5], (0, 0))
            res = -1
            pygame.display.update()
            print(toc(t1))
            print(count)
            break
        elif count == appear_time[5]:
            # 显示刺激照片6480
            window.blit(imagebox2[6], (0, 0))
            res = -1
            pygame.display.update()
            print(toc(t1))
            print(count)
            break
    if res >=0:
        window.blit(imagebox[res], (0, 0))
        # 显示背景照片
    if res > -2:
        window.blit(surface[num], (40, 120))
        # 显示问题
    if res <= -2:
        window.fill((0, 0, 0))
        window.blit(question[0],(40, 120))
        # 显示试卷
    pygame.display.update()
