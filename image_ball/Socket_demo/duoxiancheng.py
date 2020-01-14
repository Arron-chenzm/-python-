import time

import threading

def fun1(a):
    print(a)

def fun2():
    print(2222)

threads = []
threads.append(threading.Thread(target=fun1,args=(u'爱情买卖',)))
threads.append(threading.Thread(target=fun2))
print(threads)
if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()