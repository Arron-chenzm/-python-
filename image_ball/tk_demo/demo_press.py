import pygame
import sys
from pygame.locals import *
for event in pygame.event.get():
	if event.type == QUIT:
		exit()
	if event.type == KEYDOWN: # KEYDOWN 按键被按下
		if event.key == K_ESCAPE:
			print('你按下了Esc键，准备退出')
			exit()
		if event.key == K_LEFT or event.key == K_a:
			# K_LEFT：左方向键
			# K_a：A键
			print('向左移动')
		if event.key in [K_RIGHT, K_d]:
			print('向右运动')
		if event.key == K_SPACE:
			print('按下了空格键')
	elif event.type == KEYUP: # KEYUP 按键被松开
		if event.key  in [K_LEFT, K_a]:
			print('停止向左移动')
