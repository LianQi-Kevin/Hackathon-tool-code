import os

# f = open("test_name.txt", 'w')  # 先创建一个空的文本
path = "CCTSDB\\training\\enhancement_test\\images\\"  # 指定需要读取文件的目录
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
num0 = 0
for name in s:
    # print(name)
    newname = "GWB_" + str(num0) + "." + name.split('.')[1]
    os.renames(path + name, path + str(newname))
    print(str(num0) + path + name + "  ==>  " + path + newname)
    num0 += 1
