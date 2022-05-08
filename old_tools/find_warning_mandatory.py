import os


def find_warning_and_mandatory(txtpath):
    num0 = 0
    files = os.listdir(txtpath)  # 采用listdir来读取所有文件
    files.sort()  # 排序
    s = []  # 创建一个空列表
    for file_ in files:  # 循环读取每个文件名
        #    print(path +file_)
        if not os.path.isdir(txtpath + file_):  # 判断该文件是否是一个文件夹
            f_name = str(file_)
            #        print(f_name)
            s.append(f_name)  # 把当前文件名返加到列表里
            # f.write(f_name + '\n')  # 写入之前的文本中

    txtLst = []

    # print(s)
    for i in range(len(s)):
        txtFileName = s[num0]
        # print(txtFileName)
        lineCount = len(open(txtpath + txtFileName, 'r').readlines())
        if lineCount > 1:
            for a in range(lineCount):
                # print("linecount > 1")
                file = open(txtpath + txtFileName, 'r')
                lineLst = file.readline()
                lineLst = lineLst.split(' ')
                if 'mandatory' or 'warning' in lineLst:  # 定义要识别的标签
                    if txtFileName in txtLst:
                        pass
                    else:
                        txtLst.append(txtFileName)
        elif lineCount == 1:
            # print("lineCount = 1")
            file = open(txtpath + txtFileName, 'r')
            lineLst = file.readline()
            lineLst = lineLst.split(' ')
            if 'mandatory' or 'warning' in lineLst:
                txtLst.append(txtFileName)
        num0 += 1

    xmlLst = []
    for txtname in txtLst:
        xmllst = txtname.split('.')
        xmlname = str(xmllst[0] + ".xml")
        xmlLst.append(xmlname)
    # print(xmlLst)

    imgLst = []
    for txtname in txtLst:
        xmllst = txtname.split('.')
        imgname = str(xmllst[0] + ".jpg")
        imgLst.append(imgname)

    dic = [txtLst, xmlLst, imgLst]

    return dic


txtpath = "CCTSDB//training//labels//"  # 指定需要读取文件的目录
MWlst = find_warning_and_mandatory(txtpath)
print(MWlst[0])
print(MWlst[1])
print(MWlst[2])
