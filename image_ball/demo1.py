import sys, pygame
from pygame.locals import *
import time

pygame.init()#初始化pygame
size = width, height = 600, 500#窗口大小：640*480
black = 249, 130, 57
screen = pygame.display.set_mode(size)
background = pygame.image.load('2.jpg')
text = pygame.font.SysFont("宋体", 100)
text_fmt = text.render("23+56", 1, (255, 255, 255))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.blit(background, (0, 0))
        screen.blit(text_fmt, (200, 200))
        pygame.display.flip()


