
filename = "czm"
list_time_res = [1,2,3,4,5,6]
fp = open("{}.txt".format(filename), 'w')  # 如果有这个文件就打开，如果没有这个文件就创建一个名叫CSDN的txt文件
fp.write(str(list_time_res))
fp.close()