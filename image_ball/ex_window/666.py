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


pygame.init()
infoObject = pygame.display.Info()
size = width, height = infoObject.current_w,infoObject.current_h
print(width)