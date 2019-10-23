import sys, pygame
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


imagebox = []
Path = "D:\\Users\\chen\\Desktop\\new\\ciji\\database\\database2\\cat10"
files = getfiles(Path)
for i in range(0, 5):
    imagebox.append(pygame.image.load(Path + '\\' + files[i]))

while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for i in range(0, 5):
         # image_in = Image.open(imagebox[i])
         # image_out = image_in.resize(size)
        window.blit(imagebox[i], (0, 0))
        pygame.display.update()
        time.sleep(0.1)