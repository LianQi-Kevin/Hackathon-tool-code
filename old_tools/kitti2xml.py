# import numpy as np
import os
import cv2

# f = open("test_name.txt", 'w')  # 先创建一个空的文本
path = "New_Tsinghua\\PathF\\labels\\"  # 指定需要读取文件的目录
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
# print(len(s))
labelxmlPath = "New_Tsinghua\\PathF\\labels_xml\\"

num0 = 0
# while True:
for a in range(lstnum):
    # 逐个抽取列表内元素
    labelFileName = s[num0]
    num0 += 1
    # print(labelFileName)
    labelFileNamelst = labelFileName.split(".")
    # print(Blst)
    imgName = str(labelFileNamelst[0]) + ".jpg"
    # print(imgName)
    imgPath = "New_Tsinghua\\PathF\\images\\"
    print(imgPath + imgName)
    img = cv2.imread(imgPath + imgName)
    # print(img)
    imgshape = img.shape
    imgHigh = imgshape[0]
    imgWeight = imgshape[1]
    imgDepth = imgshape[2]
    # print(imgHigh)
    # print(imgWeight)

    # cv2.imshow("img",img)

    # cv2.waitKey(0)
    labelFileName_xml = labelFileNamelst[0] + ".xml"
    # print(type(labelFileNamelst))
    # print(labelFileName_xml)

    fileWrite = open(labelxmlPath + labelFileName_xml, "w")

    head = "<annotation>" + '\n' + "    <filename>" + str(imgName) + \
           "</filename>" + '\n' + "    <source>" + '\n' + "        <database>" \
           + "Unknow" + "</database>" + '\n' + "    </source>" + '\n' + "    <size>" \
           + '\n' + "        <width>" + str(imgWeight) + "</width> " + '\n' \
           + "        <height>" + str(imgHigh) + "</height>" + '\n' + "        <depth>" \
           + str(imgDepth) + "</depth>" + '\n' + "    </size>" + '\n' + "    <segmented>" + "0" + "</segmented>" + '\n'

    fileWrite.write(head)

    labelFile = path + str(labelFileName)  # 指定kitti文件名和位置
    print(labelFile)
    print(labelFileName_xml)
    LF = open(labelFile, 'r')  # 以只读方式打开标签

    lineCount = len(open(labelFile, 'r').readlines())
    print(lineCount)
    lineCount = int(lineCount)

    if lineCount > 1:
        # num = 0
        for i in range(lineCount):
            # num += 1
            LFreadline = LF.readline()
            lineList = LFreadline.split(' ')
            print(lineList)
            Tsign = lineList[0]
            xmin = lineList[4]
            ymin = lineList[5]
            xmax = lineList[6]
            ymax = lineList[7]

            Object = "    <object>" + '\n' + "        <name>" + str(Tsign) \
                     + "</name>" + '\n' + "        <pose>" + "Unspecified" \
                     + "</pose>" + '\n' + "        <truncated>" + "0" + "</truncated>" + '\n' \
                     + "        <difficult>" + "0" + "</difficult>" + '\n' + "        <bndbox>" \
                     + '\n' + "            <xmin>" + str(xmin) + "</xmin>" + '\n' \
                     + "            <ymin>" + str(ymin) + "</ymin>" + '\n' + "            <xmax>" \
                     + str(xmax) + "</xmax>" + '\n' + "            <ymax>" + str(ymax) + "</ymax>" \
                     + '\n' + "        </bndbox>" + '\n' + "    </object> " + '\n'

            fileWrite.write(Object)

    elif lineCount == 1:
        LFreadline = LF.readline()
        # print(LFread)
        lineList = LFreadline.split(' ')
        print(lineList)
        Tsign = lineList[0]
        xmin = lineList[4]
        ymin = lineList[5]
        xmax = lineList[6]
        ymax = lineList[7]
        Object = "    <object>" + '\n' + "        <name>" + str(Tsign) \
                 + "</name>" + '\n' + "        <pose>" + "Unspecified" \
                 + "</pose>" + '\n' + "        <truncated>" + "0" + "</truncated>" + '\n' \
                 + "        <difficult>" + "0" + "</difficult>" + '\n' + "        <bndbox>" \
                 + '\n' + "            <xmin>" + str(xmin) + "</xmin>" + '\n' \
                 + "            <ymin>" + str(ymin) + "</ymin>" + '\n' + "            <xmax>" \
                 + str(xmax) + "</xmax>" + '\n' + "            <ymax>" + str(ymax) + "</ymax>" \
                 + '\n' + "        </bndbox>" + '\n' + "    </object> " + '\n'

        fileWrite.write(Object)

    Finish = "</annotation>"
    fileWrite.write(Finish)

    # if num0 >= 10:
    #     break
