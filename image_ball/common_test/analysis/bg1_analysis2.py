import matplotlib.pyplot as plt

def bg1_time(str):
    """
    :param str: 存储结果的一行字符串，string类型
    :return: 刺激出现的时间，int类型，单位为1/60s
    """
    time = ""
    for char in str:
        if char != "\t":
            time = time+char
        elif char == "\t":
            break
    return int(time)

def bg1_res(str):
    """
    :param str: str: 存储结果的一行字符串，string类型
    :return: 判断的结果是否出现，string类型
    """
    res = ""
    length = len(str)
    flag = False
    for i in range(0,length):
        if str[i] != ":":
            continue
        elif str[i] == ":" and flag==False:
            flag = True
            continue
        elif str[i] == ":" and flag ==True:
            while(str[i+1]!=" "and i<length-1):
                i = i+1
                res = res+str[i]
            break
    return res

def bg1_thing(str):
    res = ""
    length = len(str)
    flag = 0
    for i in range(0, length):
        if str[i] != ":":
            continue
        elif str[i] == ":" and flag < 2:
            flag = flag+1
            continue
        elif str[i] == ":" and flag == 2:
            while (i<length-2):
                i = i + 1
                res = res + str[i]
            break
    return res

def getresult(time_list,path):
    stimu_delaytime = time_list
    fp = open(path, 'r', encoding='utf-8')
    lines = fp.readlines()
    ciji_times = [0, 0, 0, 0, 0, 0, 0]
    result = [0, 0, 0, 0, 0, 0, 0]
    acc = [0, 0, 0, 0, 0, 0, 0]
    for i in range(0, len(lines) - 1):
        time = bg1_time(lines[i])
        res = bg1_res(lines[i])
        thing = bg1_thing(lines[i])
        # print(time)
        # print(res)
        # print(thing)
        if time == stimu_delaytime[0]:
            ciji_times[0] = ciji_times[0] + 1
            if res == "未看到":
                result[0] = result[0] + 1
        for j in range(1, 7):
            if time == stimu_delaytime[j]:
                ciji_times[j] = ciji_times[j] + 1
                if res == "看到" and thing == "蝴蝶":
                    result[j] = result[j] + 1
                elif res == "看到" and thing == "不确定":
                    result[j] = result[j] + 0.5
    for i in range(0, len(result)):
        acc[i] = result[i] / ciji_times[i]
    return acc,result,ciji_times


stimu_delaytime1 = [0,2,3,4,5,9,12]
stimu_delaytime2 = [0,2,4,6,8,10,12,20]#2
stimu_delaytime3 = [0,3,6,9,12,15,20]#3
stimu_delaytime4 = [0,4,8,12,16,20,30]#4
stimu_delaytime5 = [0,5,10,15,20,25,40]#5
stimu_delaytime6 = [130,130,130,130,130,130,130]#6
path1 = '../result/dt_bg1_100_time1.txt'
path2 = '../result/dt_bg1_100_time2.txt'
path3 = '../result/dt_bg1_100_time3.txt'
path4 = '../result/dt_bg1_100_time4.txt'
path5 = '../result/dt_bg1_100_time5.txt'
path6 = '../result/dt_bg1_100_time6.txt'
(acc1,result1,ciji_times1) = getresult(stimu_delaytime1,path1)
(acc2,result2,ciji_times2) = getresult(stimu_delaytime2,path2)
(acc3,result3,ciji_times3) = getresult(stimu_delaytime3,path3)
(acc4,result4,ciji_times4) = getresult(stimu_delaytime4,path4)
(acc5,result5,ciji_times5) = getresult(stimu_delaytime5,path5)
(acc6,result6,ciji_times6) = getresult(stimu_delaytime6,path6)
plt.figure(1)
plt.plot(stimu_delaytime1,acc1)
plt.figure(2)
plt.plot(stimu_delaytime2[0:7],acc2)
plt.figure(3)
plt.plot(stimu_delaytime3,acc3)
plt.figure(4)
plt.plot(stimu_delaytime4,acc4)
plt.figure(5)
plt.plot(stimu_delaytime5,acc5)
plt.show()

