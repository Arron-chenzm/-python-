import tkinter as tk  # 使用Tkinter前需要先导入
from PIL import Image, ImageTk
import os
from tkinter import *

window = tk.Tk()
window.title('My Window')
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
size = '%dx%d' % (screenwidth, screenheight)
window.geometry(size)
def non():
    print(1)


frame1 = tk.Frame(height = 200, width=300,bg = 'red')
frame2 = tk.Frame(height = 200, width=300,bg = 'green')
frame3 = tk.Frame(height=400, width=100,bg = 'blue')
frame1.grid(row=0, column=0)
frame1.pack_propagate(0)
frame2.grid(row=1, column=0)
frame2.pack_propagate(0)
frame3.grid(row=0, column=1, rowspan=2)
frame3.pack_propagate(0)





# image_label = tk.Label(frame1,)

button1 = tk.Button(frame2, text='Cancel')
# button2 = tk.Button(frame2, text='Cancel', height=int(0.15 * screenheight), width=int(0.85 / 4 * screenwidth))
# button3 = tk.Button(frame2, text='Cancel', height=int(0.15 * screenheight), width=int(0.85 / 4 * screenwidth))
# button4 = tk.Button(frame2, text='Cancel', height=int(0.15 * screenheight), width=int(0.85 / 4 * screenwidth))
button1.pack(side=LEFT);
# button2.pack()
# button3.pack()
# button4.pack()








# message_show_Frame.grid(row=0, column=0)
# message_send_Frame.grid(row=1, column=0)
# button_Frame.grid(row=2, column=0)
# pic_right_Frame.grid(row=0, column=1, rowspan=3)

















window.mainloop()