import os
import pandas as pd

# f = open("test_name.txt", 'w')  # 先创建一个空的文本
path = "Tsinghua//training//labels//"  # 指定需要读取文件的目录
files = os.listdir(path)  # 采用listdir来读取所有文件
files.sort()  # 排序
s = []  # 创建一个空列表
for file_ in files:  # 循环读取每个文件名
    #    print(path +file_)
    if not os.path.isdir(path + file_):  # 判断该文件是否是一个文件夹
        f_name = str(file_)
        #        print(f_name)
        s.append(f_name)  # 把当前文件名返加到列表里
        # f.write(f_name + '\n')  # 写入之前的文本中
# print(s)
lstnum = len(s)
# lstnum = 10
# print(lstnum)
num0 = 0
range0 = 0
labelLst = []

for a in range(lstnum):
    Labels = open(path + s[num0], 'r')
    lineCount = len(open(path + s[num0], 'r').readlines())
    # print(lineCount)
    lineCount = int(lineCount)
    if lineCount > 1:
        for b in range(lineCount):
            labels = Labels.readline()
            labels = labels.split(' ')
            # print(type(labels))
            labelLst.append(labels[0])
        range0 += lineCount
    elif lineCount == 1:
        labels = Labels.readline()
        labels = labels.split(' ')
        labelLst.append(labels[0])
        range0 += 1
    num0 += 1

# print(str(num0) + "  " + str(range0) +  "  " +  str(labelLst))
print("Total number of files: " + str(num0) + '\n' + "Total number of labels: " + str(range0))
result = pd.value_counts(labelLst)
print(result)
