import os
import shutil
import xml.etree.ElementTree as ET


def read_xml_annotation(root, fileName):  # root 是图像路径 image_id是文件名
    in_file = open(os.path.join(root, fileName))
    tree = ET.parse(in_file)
    root = tree.getroot()
    bndboxlist = []

    for object in root.findall('object'):  # 找到root节点下的所有country节点
        bndbox = object.find('bndbox')  # 子节点下节点rank的值

        # xmin = int(bndbox.find('xmin').text)
        # xmax = int(bndbox.find('xmax').text)
        # ymin = int(bndbox.find('ymin').text)
        # ymax = int(bndbox.find('ymax').text)
        xmin = bndbox.find('xmin').text
        xmax = bndbox.find('xmax').text
        ymin = bndbox.find('ymin').text
        ymax = bndbox.find('ymax').text
        # print(xmin,ymin,xmax,ymax)
        bndboxlist.append([xmin + ".00", ymin + ".00", xmax + ".00", ymax + ".00"])
        # print(bndboxlist)
    try:
        bndbox = root.find('object').find('bndbox')
    except:
        pass
    return bndboxlist


def change_xml_list_annotation(root, fileName, new_target, saveroot):
    in_file = open(os.path.join(root, str(fileName)))  # 这里root分别由两个意思
    tree = ET.parse(in_file)
    elem = tree.find('filename')
    elem.text = (str(fileName.split('.')[0] + '.jpg'))
    xmlroot = tree.getroot()

    index = 0
    for object in xmlroot.findall('object'):  # 找到root节点下的所有country节点
        bndbox = object.find('bndbox')  # 子节点下节点rank的值
        try:
            new_xmin = new_target[index][0]
            new_ymin = new_target[index][1]
            new_xmax = new_target[index][2]
            new_ymax = new_target[index][3]
        except:
            new_xmin = new_target[0]
            new_ymin = new_target[1]
            new_xmax = new_target[2]
            new_ymax = new_target[3]
        xmin = bndbox.find('xmin')
        xmin.text = str(new_xmin)
        ymin = bndbox.find('ymin')
        ymin.text = str(new_ymin)
        xmax = bndbox.find('xmax')
        xmax.text = str(new_xmax)
        ymax = bndbox.find('ymax')
        ymax.text = str(new_ymax)

        index += 1

    # os.remove(root + fileName)
    tree.write(os.path.join(root, fileName))
    # tree.write(os.path.join(saveroot,oldname))


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


def read_fileName_in_path(pa、


    th):
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

XML_DIR = "Tsinghua\\training\\labels_xml\\"
IMG_DIR = "Tsinghua\\training\\images\\"
# TEST_DIR = "Tsinghua\\training\\labels_xml_test"
fileNameLst = read_fileName_in_path(XML_DIR)
print(fileNameLst)
# print(fileNameLst)
num0 = 0
emptyLst = []
for filename in fileNameLst:
    print(filename)
    bndbox = read_xml_annotation(XML_DIR, filename)
    newBndbox = []
    if len(bndbox) > 1:
        for lst in bndbox:
            # print(lst)
            newLst = []
            for item in lst:
                item = item.split('.')[0]
                newLst.append(item)
            newBndbox.append(newLst)
        print(newBndbox)
    elif len(bndbox) == 1:
        # print(lst)
        for item in bndbox[0]:
            item = item.split('.')[0]
            newBndbox.append(item)
        print(newBndbox)
    change_xml_list_annotation(XML_DIR, filename, newBndbox, XML_DIR)
