import os


def removefile(fromPath, removePath):
    fromLst = os.listdir(fromPath)
    removedLst = os.listdir(removePath)
    num0 = 0
    for fileName in removedLst:
        NewFileName = fileName.split('.')[0] + "." + fromLst[0].split('.')[1]
        if NewFileName not in fromLst:
            os.remove(removePath + fileName)
            print("already remove " + fileName)
            num0 += 1
    print("already remove " + str(num0) + " files")
    return


fromPath = "training//images//"
removedPath = "training//labels//"
# labels
removefile(fromPath, removedPath)
