import sys, pygame
import threading
import time
import os
from pygame.locals import *
from PIL import ImageTk, Image

pygame.init()

pygame.font.init()
size = width, height = 500, 330
window = pygame.display.set_mode(size)
window1 = pygame.display.set_mode(size)

def getfiles(Path):
    """获取图片文件名。"""
    files = os.listdir(Path)
    for x in files:
        if not (x.endswith('.jpg') or x.endswith('.JPG') or x.endswith('.png')):
            files.remove(x)
    return files


def img_change():
    imagebox = []
    Path = "D:\\Users\\chen\\Desktop\\new\\ciji\\database\\database2\\cat10"
    files = getfiles(Path)
    for i in range(0, 5):
        imagebox.append((pygame.image.load(Path + '\\' + files[i])).convert())
    while (True):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        for i in range(0, 5):
            # image_in = Image.open(imagebox[i])
            # image_out = image_in.resize(size)
            window.blit(imagebox[i], (0, 0))
            pygame.display.flip()
            time.sleep(3)


def font_change():
    text = pygame.font.SysFont("宋体", 100)
    text_fmt = text.render("23+56", 1, (255, 255, 255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        window.blit(text_fmt, (200, 150))
        pygame.display.flip()
        time.sleep(3)
f = threading.Thread(target=font_change)
t = threading.Thread(target=img_change)

f.start()
t.start()









