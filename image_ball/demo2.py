import os


def getfiles(Path):
    """获取图片文件名。"""
    files = os.listdir(Path)
    for x in files:
        if not (x.endswith('.jpg') or x.endswith('.JPG') or x.endswith('.png')):
            files.remove(x)
    return files
Path = "D:\\Users\\chen\Desktop\\new\\ciji\\database\\database1\\airliner01"
files = getfiles(Path)
for i in range(0,100):
    print(files[i])
