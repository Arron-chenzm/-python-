import tkinter as tk  # 使用Tkinter前需要先导入
from PIL import Image, ImageTk
import os

window = tk.Tk()
frame1 = tk.Frame(height = 200, width=300,bg = 'red') # 创建<消息列表分区 >
frame2 = tk.Frame(height = 200, width=300,bg = 'blue') # 创建<发送消息分区 >
frame3 = tk.Frame(height=400, width=100,bg = 'red')      # 创建<图片分区>

def msgsendEvent():
    print(4)
##  Frame在主控件上的布局
frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)

frame3.grid(row=0, column=1, rowspan=2)
button_send = tk.Button(frame1, text='Send')
button_send.grid(row=0, column=0)

tk.mainloop()