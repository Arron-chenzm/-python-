

import tkinter as tk  # 使用Tkinter前需要先导入
from PIL import Image, ImageTk
import os


window = tk.Tk()# 第1步，实例化object，建立窗口window
window.title('My Window')# 第2步，给窗口的可视化起名字
window.geometry('500x600')  # 这里的乘是小x# 第3步，设定窗口的大小(长 * 宽)
# 第4步，在图形界面上设定标签
var = tk.StringVar()  # 用.set()和.get()来设置和得到label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(window, textvariable= var , bg='green', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
# 第5步，放置标签
l.pack()  # Label内容content区域放置位置，自动调节尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();
def getfiles(Path):
    """获取图片文件名。"""
    files = os.listdir(Path)
    for x in files:
        if not (x.endswith('.jpg') or x.endswith('.JPG') or x.endswith('.png')):
            files.remove(x)
    return files
Path = "D:\\Users\\chen\Desktop\\new\\ciji\\database\\database1\\airliner01"
files = getfiles(Path)
img_open = Image.open(Path+'/'+files[1])
img_png = ImageTk.PhotoImage(img_open)
label_img = tk.Label(window, textvariable= var, font=('Arial', 12),compound = 'center',image = img_png)
label_img.pack()
on_hit = False
def hit_me():
    global on_hit
    if on_hit==False:
        on_hit = True
        var.set("dian a!")
    else:
        on_hit = False
        var.set("happy")
button1 = tk.Button(window,text ='hit me',font=('Arial', 12), width=10, height=1, command=hit_me)
button1.pack();



# 第6步，主窗口循环显示
window.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
