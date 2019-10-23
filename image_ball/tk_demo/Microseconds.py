import datetime
oldtime=datetime.datetime.now()
print(oldtime)
x=1
while x<100000000:
    x=x+1
newtime=datetime.datetime.now()
def toc(t1):
    t2 = datetime.datetime.now()
    return (t2-t1).microseconds

print(newtime)
print(u'相差：%s'%(newtime-oldtime))
print(u'相差：%s微秒'%(newtime-oldtime).microseconds)
print(u'相差：%s微秒'%(toc(oldtime)))
print((newtime-oldtime).microseconds/1000)
print(u'相差：%s秒'%(newtime-oldtime).seconds)

