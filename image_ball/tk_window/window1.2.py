import tkinter as tk  # 使用Tkinter前需要先导入
from tkinter import *
# from PIL import Image, ImageTk
# import os

root = Tk();
fm1 = Frame(root)
Button(fm1, text='Top').pack(side=TOP, anchor=W, fill=X, expand=YES)
Button(fm1, text='Center').pack(side=TOP, anchor=W, fill=X, expand=YES)
Button(fm1, text='Bottom').pack(side=TOP, anchor=W, fill=X, expand=YES)
fm1.pack(side=LEFT, fill=BOTH, expand=YES)

fm2 = Frame(root)
Button(fm2, text='Left').pack(side=LEFT)
Button(fm2, text='This is the Center button').pack(side=LEFT)
Button(fm2, text='Right').pack(side=LEFT)
fm2.pack(side=LEFT, padx=10)
root.mainloop()
