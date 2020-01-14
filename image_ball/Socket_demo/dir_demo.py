import os

def getfiles(Path):
    """获取图片文件名。"""
    files = os.listdir(Path)
    for x in files:
        if not (x.endswith('.jpg') or x.endswith('.JPG') or x.endswith('.png')):
            files.remove(x)
    return files
path = "D:\\Users\\chen\\Desktop\\iceframe\\frames"
files = getfiles(path)
for i in range(0,100):
    print(files[i])