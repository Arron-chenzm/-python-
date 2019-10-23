import tkinter as tk  # 使用Tkinter前需要先导入
from PIL import Image, ImageTk
import os
import datetime
import time




window = tk.Tk()# 第1步，实例化object，建立窗口window
window.title('My Window')# 第2步，给窗口的可视化起名字
window.geometry('500x400')  # 这里的乘是小x# 第3步，设定窗口的大小(长 * 宽)
canvas=tk.Canvas(window,width=500,height=500,bg = 'white')
def getfiles(Path):
    """获取图片文件名。"""
    files = os.listdir(Path)
    for x in files:
        if not (x.endswith('.jpg') or x.endswith('.JPG') or x.endswith('.png')):
            files.remove(x)
    return files
Path = "D:\\Users\\chen\Desktop\\new\\ciji\\database\\database1\\airliner01"
files = getfiles(Path)
# img_open = Image.open(Path+'/'+files[1])
# img_png = ImageTk.PhotoImage(img_open)
# label_img = tk.Label(window,  font=('Arial', 12),compound = 'center',image = img_png)
# label_img.pack()

def toc(t1):
    t = time.time()
    return (t-t1)*1000
t1 = time.time()
t2 = 0
for i in range(1,20):
    img_open = Image.open(Path + '/' + files[i])
    img_png = ImageTk.PhotoImage(img_open)
    # t2 = toc(t1)
    while t2<1000*i:

        t2 = toc(t1)
        # print(t2)
    # label_img = tk.Label(window, font=('Arial', 12), compound='center', image=img_png)
    # label_img.pack()

    itext = canvas.create_image((250, 150), image=img_png)
    print(t2)
    print(i)

    canvas.pack()
    window.update()




window.mainloop()