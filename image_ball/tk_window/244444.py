import random
list_time_res = [0] * 80
print(list_time_res)
print(len(list_time_res))
fp = open("{}.txt".format("czm"), 'a')
for i in range(0, len(list_time_res)-2):

    fp.writelines("{}\n".format(list_time_res[i]))
    print(i)
    # tem = str(stimu_delaytime_list[i])
    # fp.write(tem)
fp.close()