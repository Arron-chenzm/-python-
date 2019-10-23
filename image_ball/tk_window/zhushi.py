from tkinter import *
import os
from PIL import Image, ImageTk

window = Tk()
screenwidth = window.winfo_screenwidth()#1920
screenheight = window.winfo_screenheight()#1080
size = '%dx%d' % (screenwidth, screenheight-80)
window.geometry(size)

def getfiles(Path):
    """获取图片文件名。"""
    files = os.listdir(Path)
    for x in files:
        if not (x.endswith('.jpg') or x.endswith('.JPG') or x.endswith('.png')):
            files.remove(x)
    return files
Path = "D:\\Users\\chen\\Desktop\\new\\ciji\\database\\database2\\cat10"
files = getfiles(Path)
# img_open = Image.open(Path+'/'+files[1]).resize((1700,900),Image.ANTIALIAS)
img_open = Image.open('D:\\Users\\chen\\Desktop\\figure\\dog2.jpg').resize((1700,900),Image.ANTIALIAS)
# img_open = Image.open('D:\\Users\\chen\\Desktop\\figure\\noise.png').resize((1700,900),Image.ANTIALIAS)
img_png = ImageTk.PhotoImage(img_open)


fm1 = Frame(window,height = 900, width=1700,bg = 'yellow')
label_image = Label(window,image =img_png,text = '43-23= 30? ',font=('Arial', 200),fg='white',compound = CENTER  ,height = 900, width=1700)
label_image.grid(row=0, column=0)
# fm1.pack(side=LEFT, fill=BOTH, expand=YES)
fm1.grid(row=0, column=0)
fm1.pack_propagate(0)

fm2 = Frame(window ,height = 1080-80, width=220)
# Label(fm2,text='阈下刺激帧时长(ms)',height = 3).pack(side=TOP,pady = 0, fill=X, expand=NO)
Scale(fm2, label='阈下刺激帧时长(ms)', from_=40, to=800, orient=HORIZONTAL,tickinterval=760,
          resolution=1).pack(side=TOP, pady = 4,fill=X, expand=NO)
# var1=StringVar()
# entry1 = Entry(fm2,textvariable=var1)
# entry1.pack(side=TOP, pady = 4,fill=X, expand=NO)
Label(fm2,text='重复次数',height = 3).pack(side=TOP, pady = 0,fill=X, expand=NO)
Entry(fm2,).pack(side=TOP,pady = 4, fill=X, expand=NO)
s = Scale(fm2, label='刺激帧出现时机', from_=0, to=15, orient=HORIZONTAL,tickinterval=15,
          resolution=1).pack(side=TOP, pady = 4,fill=X, expand=NO)

Label(fm2,text='阈下刺激内容',height = 3).pack(side=TOP, pady = 4,fill=X, expand=NO)

varciji = StringVar()
Radiobutton(fm2, text='苹果', variable=varciji, value='A').pack(side=TOP, pady = 0,fill=X, expand=NO)
Radiobutton(fm2, text='梨', variable=varciji, value='B').pack(side=TOP, pady = 0,fill=X, expand=NO)
Radiobutton(fm2, text='火龙果', variable=varciji, value='C').pack(side=TOP, pady = 0,fill=X, expand=NO)
Radiobutton(fm2, text='香蕉', variable=varciji, value='D').pack(side=TOP, pady = 0,fill=X, expand=NO)
Radiobutton(fm2, text='随机', variable=varciji, value='E').pack(side=TOP, pady = 0,fill=X, expand=NO)
Label(fm2,height = 4).pack(side=TOP, pady = 0,fill=X, expand=NO)

Label(fm2,text='背景视频内容',height = 3).pack(side=TOP, pady = 4,fill=X, expand=NO)

varbg = StringVar()
Radiobutton(fm2, text='猫', variable=varbg, value='A').pack(side=TOP, pady = 0,fill=X, expand=NO)
Radiobutton(fm2, text='狗', variable=varbg, value='B').pack(side=TOP, pady = 0,fill=X, expand=NO)
Radiobutton(fm2, text='白噪声', variable=varbg, value='C').pack(side=TOP, pady = 0,fill=X, expand=NO)
Radiobutton(fm2, text='光栅', variable=varbg, value='D').pack(side=TOP, pady = 0,fill=X, expand=NO)

# sig1 = StringVar()
# sig1.set('阈下:')
# Label(fm2,textvariable = sig1,height = 4).pack(side=TOP, pady = 0,fill=X, expand=NO)

def show():
    pass



Button(fm2, text='START', font=('Arial', 25),height=3,command = show(),relief = SUNKEN).pack(side=BOTTOM, pady=20, fill=X, expand=NO)
fm2.grid(row=0, column=1, rowspan=2)
fm2.pack_propagate(0)

fm3 = Frame(window ,height = 180-80, width=1700,bg = 'red')
Button(fm3, text='正确(A)',font=('Arial', 25),padx = 10,relief = SUNKEN).pack(side=LEFT, fill=BOTH, expand=YES)
Button(fm3, text='错误(L)',font=('Arial', 25),padx = 10,relief = SUNKEN).pack(side=LEFT, fill=BOTH, expand=YES)

fm3.grid(row=1, column=0)
fm3.pack_propagate(0)
# fm3.pack(side=LEFT, fill=BOTH, expand=YES)










window.mainloop()