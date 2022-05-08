import os
import shutil


def read_fileName_in_path(path):
    files = os.listdir(path)  # 采用listdir来读取所有文件
    files.sort()  # 排序
    fileNameLst = []  # 创建一个空列表
    for file_ in files:  # 循环读取每个文件名
        #    print(path +file_)
        if not os.path.isdir(path + file_):  # 判断该文件是否是一个文件夹
            f_name = str(file_)
            #        print(f_name)
            fileNameLst.append(f_name)  # 把当前文件名返加到列表里
            # f.write(f_name + '\n')  # 写入之前的文本中
    return fileNameLst


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


xmlPath = "New_Tsinghua//labels_xml//"
imgPath = "New_Tsinghua//images//"

outPutPathA = "New_Tsinghua//PathA//"
outPutPathB = "New_Tsinghua//PathB//"
outPutPathC = "New_Tsinghua//PathC//"
outPutPathD = "New_Tsinghua//PathD//"
outPutPathE = "New_Tsinghua//PathE//"
outPutPathF = "New_Tsinghua//PathF//"
outPutPathG = "New_Tsinghua//PathG//"
outPutPathH = "New_Tsinghua//PathH//"
outPutPathI = "New_Tsinghua//PathI//"
num0 = 0
pathLst = (
outPutPathA, outPutPathB, outPutPathC, outPutPathD, outPutPathE, outPutPathF, outPutPathG, outPutPathH, outPutPathI)
for path in pathLst:
    mkdir(path)
for name in read_fileName_in_path(xmlPath):
    if num0 <= 2700:
        pathname = pathLst[0]
    elif num0 > 2700 and num0 <= 5400:
        pathname = pathLst[1]
    elif num0 > 5400 and num0 <= 8100:
        pathname = pathLst[2]
    elif num0 > 8100 and num0 <= 10800:
        pathname = pathLst[3]
    elif num0 > 10800 and num0 <= 13500:
        pathname = pathLst[4]
    elif num0 > 13500 and num0 <= 16200:
        pathname = pathLst[5]
    elif num0 > 16200 and num0 <= 18900:
        pathname = pathLst[6]
    elif num0 > 18900 and num0 <= 21600:
        pathname = pathLst[7]
    elif num0 > 21600 and num0 <= 24300:
        pathname = pathLst[8]
    shutil.copy(os.path.join(xmlPath, name), pathname)
    shutil.copy(os.path.join(imgPath, name[:-4] + '.jpg'), pathname)
    print("num = " + str(num0) + " Finish copy " + name + " to " + pathname)
    num0 += 1
