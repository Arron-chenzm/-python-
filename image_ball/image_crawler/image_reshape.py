import os

from PIL import Image

class BatchReshape:
    def __init__(self):
        self.inpath = "D:\\Users\\chen\\Desktop\\new\\ciji\\database\\database2\\cat10"
        self.outpath = "D:\\Users\\chen\\Desktop\\new\\ciji\\database\\database2\\cat11"
        if not os.path.exists(self.outpath):
            os.makedirs(self.outpath)
            print("{}创建成功".format(self.outpath))

    def reshape(self):
        filelist = os.listdir(self.inpath)
        count = 0
        for item in filelist:
            if item.endswith('.jpg'):
                infile = os.path.join(os.path.abspath(self.inpath),item)
                outfile = os.path.join(os.path.abspath(self.outpath),item)
            try:
                im = Image.open(infile)
                out = im.resize((500,330),Image.ANTIALIAS)
                out.save(outfile)
                count = count+1
                print("第{}张reshaping......".format(count))
            except:
                print("第{}张reshap失败.".format(count))
                count = count+1
                continue
        print("任务结束，共处理{}张图片".format(count))
if __name__ == '__main__':
    demo = BatchReshape()
    demo.reshape()