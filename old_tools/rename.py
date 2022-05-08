import os


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


def renamesNewName(path, name, oldname):
    path = str(path)
    name = str(name)
    oldname = str(oldname)
    os.renames(path + name, path + oldname)
    newnameLst = [name, oldname]
    return newnameLst


IMG_DIR = "CCTSDB//training//enhancement_test//images//"
XML_DIR = "CCTSDB//training//enhancement_test//labels_xml//"
TXT_DIR = "CCTSDB//training//enhancement_test//labels//"

A = renamesOldName(XML_DIR, name)
