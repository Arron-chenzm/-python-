import os
import sys, pygame


# def getfiles(Path):
#     """获取图片文件名。"""
#     files = os.listdir(Path)
#     for x in files:
#         if not (x.endswith('.jpg') or x.endswith('.JPG') or x.endswith('.png')):
#             files.remove(x)
#     return files
# Path = "D:\\Users\\chen\\Desktop\\new\\codefile\\image_ball\\image_crawler\\Image_cat"

class BatchRename():
    def __init__(self):
        self.path = "D:\\Users\\chen\\Desktop\\new\\ciji\\database\\database2\\cat11"

    def rename(self):
        filelist = os.listdir(self.path)
        img_num = len(filelist)
        i = 54
        for item in filelist:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path),item)
                dst = os.path.join(os.path.abspath(self.path),'imageb ({}) .jpg'.format(i) )
                try:
                    os.rename(src, dst)
                    print("第{}张重命名中......".format(i))
                    i = i + 1
                except:
                    continue
        print("共{}张图片重命名结束".format(i))
if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
