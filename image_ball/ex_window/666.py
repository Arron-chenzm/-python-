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


def get_ciji(str):
    ciji = ''
    length = len(str)
    for i in range(length-2,0,-1):
        if str[i]!= ' ':
            ciji= str[i]+ciji
        else:
            break
    return ciji

path ='D:\\Users\\chen\\Desktop\\new\\codefile\\image_ball\\common_test\\result\\dt_test1.txt'

fp = open(path, 'r', encoding='utf-8')
lines = fp.readlines()
for i in range(0,6):
    print(get_ciji(lines[i]))
