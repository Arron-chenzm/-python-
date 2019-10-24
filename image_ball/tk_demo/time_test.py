import sys, pygame
from pygame import *
import threading
import time
import os
import random

# count = 0
# for i in range(0,100):
#       num1 = random.randint(0, 50)
#       num2 = random.randint(0, 50)
#       p =  random.uniform(0,1)
#       if p>0.5:
#             sum = num1 +num2
#             count = count+1
#       else:
#             sum = random.randint(50, 100)
#       str = "{}+{}={}?".format(num1,num2,sum)
#
#       print("{}{}{}{}{}{}{}".format(p," ",num1," ",num2," ",sum))
#       print (str)
# print(count)

def strrandom():
      num1 = random.randint(0, 50)
      num2 = random.randint(0, 50)
      p = random.uniform(0, 1)
      if p > 0.5:
            sum = num1 + num2
      else:
            sum = random.randint(50, 100)
      str = "{}+{}={}?".format(num1, num2, sum)
      return str
for i in range(0,10):
      str = strrandom()
      print(str)