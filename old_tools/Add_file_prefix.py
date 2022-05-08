import os

path = "CCTSDB\\training\\labels\\"  # 指定需要读取文件的目录
# path = input("请输入要更改的文件的路径: ")
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
# filePrefix = input("请输入要添加的文件前缀: ")
filePrefix = "CCTSDB_"  # 要使用的前缀

# print("Number of lists: " + str(len(s)))
num0 = 0
for a in range(len(s)):
    fileName = s[num0]
    # print(fileName)
    num0 += 1
    os.renames(path + fileName, path + filePrefix + fileName)
    print(filePrefix + fileName)
print("Changes are complete! Altogether changed: " + str(len(s)))
