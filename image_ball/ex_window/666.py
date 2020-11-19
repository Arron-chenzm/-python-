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
trail_times = 91
ciji_shape = 4
width = 1920
height = 1080
ciji_wzx = []
ciji_wzy = []
for i in range(0,trail_times):
    pic_local = random.randint(1,4)
    if pic_local == 1:
        ciji_wzx.append(random.randint(0,int((ciji_shape-1) * width / ciji_shape)-10))
        ciji_wzy.append(0)
    elif pic_local == 2:
        ciji_wzx.append(random.randint(0,int((ciji_shape-1) * width / ciji_shape)-10))
        ciji_wzy.append(int((ciji_shape-1) * height / ciji_shape)-10)
    elif pic_local == 3:
        ciji_wzx.append(0)
        ciji_wzy.append(random.randint(0,int((ciji_shape-1) * height / ciji_shape)-10))
    elif pic_local == 4:
        ciji_wzx.append(int((ciji_shape-1) * width / ciji_shape)-10)
        ciji_wzy.append( random.randint(0,int((ciji_shape-1) * height / ciji_shape)-10))


