import tkinter as tk  # 使用Tkinter前需要先导入
from PIL import Image, ImageTk
import os


def resize(w, h, w_box, h_box, im):
    f1 = 1.0 * w_box / w
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return im.resize((width, height), Image.ANTIALIAS)

window = tk.Tk()
window.title('My Window')
window.geometry('500x600')
canvas=tk.Canvas(window,width=500,height=500,bg = 'white')

var = tk.StringVar()  # 用.set()和.get()来设置和得到label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=30, height=2)
l.pack()  # Label内容content区域放置位置，自动调节尺寸


# 放置lable的方法有：1）l.pack(); 2)l.place();

def getfiles(Path):
    files = os.listdir(Path)
    for x in files:
        if not (x.endswith('.jpg') or x.endswith('.JPG') or x.endswith('.png')):
            files.remove(x)
    return files

Path = "D:\\Users\\chen\\Desktop\\new\\ciji\\database\\database2\\cat10"
files = getfiles(Path)
# img_open = Image.open(Path+'/'+files[1])
# img_png = ImageTk.PhotoImage(img_open)
# label_img = tk.Label(window, textvariable= var, font=('Arial', 12),compound = 'center',image = img_png)
# label_img.pack()

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
button1.pack()

for i in range(1,10):
    img_open = Image.open(Path + '/' + files[i])
    img_png = ImageTk.PhotoImage(img_open)
    # label_img = tk.Label(window, textvariable=var, font=('Arial', 12), compound='center', image=img_png)
    # label_img.pack()
    itext = canvas.create_image((250, 150), image=img_png)
    canvas.pack()
    
    window.update()
    window.after(3000)






window.mainloop()

