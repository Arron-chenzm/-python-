import pygame

from Button import Button


# 初始化pygame
pygame.init()
winSur = pygame.display.set_mode([500, 500])

# 加载按钮图片
surBtnNormal = pygame.image.load("./btn_normal.png").convert_alpha()
surBtnMove = pygame.image.load("./btn_move.png").convert_alpha()
surBtnDown = pygame.image.load("./btn_down.png").convert_alpha()

# 按钮使用的字体
btnFont = pygame.font.SysFont("lisu", 40)

list = []
# 按钮的回调函数
def btnCallBack1():
    list.append('cat')
    print("我被按下了")
    print(list)
def btnCallBack2():
    list.append('cat')
    print("我被按下了")
    print(list)


# 创建按钮
btn1 = Button(0, 0, "猫", surBtnNormal, surBtnMove, surBtnDown, btnCallBack1, btnFont, (255, 0, 0))
btn2 = Button(200, 0, "狗", surBtnNormal, surBtnMove, surBtnDown, btnCallBack2, btnFont)
btn3 = Button(100, 200, "下一个", surBtnNormal, surBtnMove, surBtnDown, btnCallBack2, btnFont)

# 游戏主循环
while True:
    mx, my = pygame.mouse.get_pos()  # 获得鼠标坐标

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEMOTION:  # 鼠标移动事件
            # 判断鼠标是否移动到按钮范围内
            btn1.getFocus(mx, my)
            btn2.getFocus(mx, my)
            btn3.getFocus(mx, my)

        elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标按下
            if pygame.mouse.get_pressed() == (1, 0, 0):  # 鼠标左键按下
                btn1.mouseDown(mx, my)
                btn2.mouseDown(mx, my)
                btn3.mouseDown(mx, my)

        elif event.type == pygame.MOUSEBUTTONUP:  # 鼠标弹起
            btn1.mouseUp()
            btn2.mouseUp()
            btn3.mouseUp()

    pygame.time.delay(16)
    winSur.fill((0, 0, 0))
    # 绘制按钮
    btn1.draw(winSur)
    btn2.draw(winSur)
    btn3.draw(winSur)
    # 刷新界面
    pygame.display.flip()
