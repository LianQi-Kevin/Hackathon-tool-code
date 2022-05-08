import os
import shutil
import xml.etree.ElementTree as ET

import imgaug as ia
import numpy as np
from PIL import Image
from imgaug import augmenters as iaa

ia.seed(1)


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

    mandatoryLst = []
    warningLst = []
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
                if 'warning' in lineLst:  # 定义要识别的标签
                    if txtFileName in warningLst:
                        pass
                    else:
                        warningLst.append(txtFileName)
                elif 'mandatory' in lineLst:
                    if txtFileName in mandatoryLst:
                        pass
                    else:
                        mandatoryLst.append(txtFileName)
        elif lineCount == 1:
            # print("lineCount = 1")
            file = open(txtpath + txtFileName, 'r')
            lineLst = file.readline()
            lineLst = lineLst.split(' ')
            if 'mandatory' in lineLst:
                mandatoryLst.append(txtFileName)
            elif 'warning' in lineLst:
                warningLst.append(txtFileName)
        num0 += 1

        for name in warningLst:
            if name in mandatoryLst:
                num = mandatoryLst.index(name)
                mandatoryLst.pop(num)

    mandatoryxmlLst = []
    for txtname in mandatoryLst:
        xmllst = txtname.split('.')
        xmlname = str(xmllst[0] + ".xml")
        mandatoryxmlLst.append(xmlname)
    # print(xmlLst)
    warningxmlLst = []
    for txtname in warningLst:
        xmllst = txtname.split('.')
        xmlname = str(xmllst[0] + ".xml")
        warningxmlLst.append(xmlname)
    # print(xmlLst)

    mandatoryimgLst = []
    for txtname in mandatoryLst:
        xmllst = txtname.split('.')
        imgname = str(xmllst[0] + ".jpg")
        mandatoryimgLst.append(imgname)
    warningimgLst = []
    for txtname in warningLst:
        xmllst = txtname.split('.')
        imgname = str(xmllst[0] + ".jpg")
        warningimgLst.append(imgname)

    dic = [[mandatoryLst, warningLst], [mandatoryxmlLst, warningxmlLst], [mandatoryimgLst, warningimgLst]]

    return dic


# 读取xml文件内的xmin ymin xmax ymax 并创建列表
def read_xml_annotation(root, image_id):  # root 是图像路径 image_id是文件名
    in_file = open(os.path.join(root, image_id))
    tree = ET.parse(in_file)
    root = tree.getroot()
    bndboxlist = []

    for object in root.findall('object'):  # 找到root节点下的所有country节点
        bndbox = object.find('bndbox')  # 子节点下节点rank的值

        xmin = int(bndbox.find('xmin').text)
        xmax = int(bndbox.find('xmax').text)
        ymin = int(bndbox.find('ymin').text)
        ymax = int(bndbox.find('ymax').text)
        # print(xmin,ymin,xmax,ymax)
        bndboxlist.append([xmin, ymin, xmax, ymax])
        # print(bndboxlist)

    bndbox = root.find('object').find('bndbox')
    return bndboxlist


def change_xml_list_annotation(root, image_id, new_target, saveroot, id, file_Prefix, num0):
    # def change_xml_list_annotation(root, image_id, new_target, saveroot, oldname):
    in_file = open(os.path.join(root, str(image_id)))  # 这里root分别由两个意思
    tree = ET.parse(in_file)
    elem = tree.find('filename')
    elem.text = (file_Prefix + "_" + str(num0) + str("%06d" % int(id)) + '.jpg')
    xmlroot = tree.getroot()
    index = 0

    for object in xmlroot.findall('object'):  # 找到root节点下的所有country节点
        bndbox = object.find('bndbox')  # 子节点下节点rank的值

        # xmin = int(bndbox.find('xmin').text)
        # xmax = int(bndbox.find('xmax').text)
        # ymin = int(bndbox.find('ymin').text)
        # ymax = int(bndbox.find('ymax').text)

        new_xmin = new_target[index][0]
        new_ymin = new_target[index][1]
        new_xmax = new_target[index][2]
        new_ymax = new_target[index][3]

        xmin = bndbox.find('xmin')
        xmin.text = str(new_xmin)
        ymin = bndbox.find('ymin')
        ymin.text = str(new_ymin)
        xmax = bndbox.find('xmax')
        xmax.text = str(new_xmax)
        ymax = bndbox.find('ymax')
        ymax.text = str(new_ymax)

        index += 1

    tree.write(os.path.join(saveroot, file_Prefix + str(num0) + "_" + str("%06d" % int(id)) + '.xml'))
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


def renamesOldName(path, name):
    path = str(path)
    name = str(name)
    fileNameLst = name.split('.')
    filename = fileNameLst[0]
    fileExtension = str("." + fileNameLst[1])
    newname = str("000000" + fileExtension)
    os.renames(path + name, path + newname)
    oldnameLst = [name, newname]
    return oldnameLst


if __name__ == "__main__":  # 为了使该文件内的函数可以被其他文件调用的同时自身作为脚本使用
    trainingDir = "Tsinghua//training//"
    # trainingDir = input("请输入training文件夹地址: ")
    IMG_DIR = trainingDir + "images//"
    XML_DIR = trainingDir + "labels_xml//"
    TXT_DIR = trainingDir + "labels//"
    # file_Prefix = input("请输入文件前缀: ")
    file_Prefix = "mandatory_"
    xmlLst = 0  # mandatory = 0   warning = 1

    # 指定路径并调用mkdir函数判断并创建路径
    AUG_XML_DIR = trainingDir + file_Prefix + "labels_xml//"  # 存储增强后的XML文件夹路径
    try:
        shutil.rmtree(AUG_XML_DIR)
    except FileNotFoundError as e:
        a = 1
    mkdir(AUG_XML_DIR)

    AUG_IMG_DIR = trainingDir + file_Prefix + "images//"  # 存储增强后的影像文件夹路径
    try:
        shutil.rmtree(AUG_IMG_DIR)
    except FileNotFoundError as e:
        a = 1
    mkdir(AUG_IMG_DIR)

    AUGLOOP = 4  # 每张影像增强的数量

    boxes_img_aug_list = []
    new_bndbox = []
    new_bndbox_list = []

    # 影像增强
    seq = iaa.Sequential([
        # iaa.Flipud(0.5),  # 垂直翻转所有图像的20％
        # iaa.Fliplr(0.5),  # 镜像
        iaa.Multiply((1.2, 1.5)),  # 改变亮度，不影响BBs
        iaa.GaussianBlur(sigma=(0, 1.0)),  # 高斯模糊
        iaa.Affine(
            translate_px={"x": 15, "y": 15},
            scale=(0.8, 0.95),
            rotate=(-30, 30)
        )  # 在x/y轴上平移40/60px，缩放到50-70％，影响BBs
    ])

    mandatoryAndWarningLst = find_warning_and_mandatory(TXT_DIR)

    num0 = 0
    for name in mandatoryAndWarningLst[1][xmlLst]:
        # print(name)
        # name = "CCTSDB_0000001.xml"
        bndbox = read_xml_annotation(XML_DIR, name)  # 使用read_xml_annotation函数提取bndbox列表
        shutil.copy(os.path.join(XML_DIR, name), AUG_XML_DIR)  # 复制xml_label
        shutil.copy(os.path.join(IMG_DIR, name[:-4] + '.jpg'), AUG_IMG_DIR)  # 复制图片

        Renamesxml = renamesOldName(AUG_XML_DIR, name)
        Renamesimg = renamesOldName(AUG_IMG_DIR, name[:-4] + '.jpg')
        xmlNewName = Renamesxml[1]
        xmlOldname = Renamesxml[0]
        imgNewName = Renamesimg[1]
        imgOldname = Renamesimg[0]

        for epoch in range(AUGLOOP):
            seq_det = seq.to_deterministic()  # 保持坐标和图像同步改变，而不是随机
            # 读取图片
            print(imgNewName)
            img = Image.open(os.path.join(AUG_IMG_DIR, imgNewName))
            # sp = img.size
            img = np.asarray(img)
            # bndbox 坐标增强
            for i in range(len(bndbox)):
                bbs = ia.BoundingBoxesOnImage([
                    ia.BoundingBox(x1=bndbox[i][0], y1=bndbox[i][1], x2=bndbox[i][2], y2=bndbox[i][3]),
                ], shape=img.shape)

                bbs_aug = seq_det.augment_bounding_boxes([bbs])[0]
                boxes_img_aug_list.append(bbs_aug)

                # new_bndbox_list:[[x1,y1,x2,y2],...[],[]]
                n_x1 = int(max(1, min(img.shape[1], bbs_aug.bounding_boxes[0].x1)))
                n_y1 = int(max(1, min(img.shape[0], bbs_aug.bounding_boxes[0].y1)))
                n_x2 = int(max(1, min(img.shape[1], bbs_aug.bounding_boxes[0].x2)))
                n_y2 = int(max(1, min(img.shape[0], bbs_aug.bounding_boxes[0].y2)))
                if n_x1 == 1 and n_x1 == n_x2:
                    n_x2 += 1
                if n_y1 == 1 and n_y2 == n_y1:
                    n_y2 += 1
                if n_x1 >= n_x2 or n_y1 >= n_y2:
                    print('error', name)
                new_bndbox_list.append([n_x1, n_y1, n_x2, n_y2])
            # 存储变化后的图片
            image_aug = seq_det.augment_images([img])[0]
            # path = os.path.join(AUG_IMG_DIR,str("%06d" % (len(files) + int(name[:-4]) + epoch * 250)) + '.jpg')
            path = os.path.join(AUG_IMG_DIR, file_Prefix + str(num0) + "_" + str("%06d" % (epoch * 250)) + '.jpg')

            image_auged = bbs.draw_on_image(image_aug, thickness=0)
            Image.fromarray(image_auged).save(path)

            # 存储变化后的XML
            # change_xml_list_annotation(XML_DIR, name[:-4], new_bndbox_list, AUG_XML_DIR, len(files) + int(name[:-4]) + epoch * 250)
            change_xml_list_annotation(AUG_XML_DIR, xmlNewName, new_bndbox_list, AUG_XML_DIR, epoch * 250, file_Prefix,
                                       str(num0))
            print(str(file_Prefix + str(num0) + "_" + str("%06d" % (epoch * 250)) + '.jpg'))
            new_bndbox_list = []

            # renamesNewName(XML_DIR, xmlNewName, xmlOldname)
            # renamesNewName(IMG_DIR, imgNewName, imgOldname)

            num0 += 1

        path1 = AUG_XML_DIR + xmlNewName
        path2 = AUG_IMG_DIR + imgNewName

        os.remove(path1)
        os.remove(path2)
