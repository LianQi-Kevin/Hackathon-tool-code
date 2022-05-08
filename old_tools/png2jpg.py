import os

from PIL import Image

inputpath = r"CCTSDB//training//images_png//"
outputpath = r"CCTSDB//training//images//"
# print(path)
num0 = 0
for name in os.listdir(inputpath):
    # print(name)
    img = Image.open(os.path.join(inputpath, name))
    file_name, file_type = os.path.splitext(name)
    imgPath = inputpath + name
    # print(imgPath)
    # print(file_type)
    # print(str(num0) + " " + inputpath + name)
    # if os.path.getsize(os.path.join(path,name))>1024*1024:
    #     w, h = img.size
    #     # 缩放到50%
    #     img.thumbnail((w//3, h//3))
    if img.mode == 'RGBA':  # 4通道转3通道
        r, g, b, a = img.split()
        img = Image.merge("RGB", (r, g, b))
        print(str(num0) + name + " is RGBA, chang finish!")
    elif img.mode != 'RGB':  # 1通道转3通道
        img = image.convert("RGB")
        os.remove(imgPath)
        img.save(imgPath)
        print(str(num0) + name + " is only 1 channel, chang finish!")
    if file_type == '.jpg':  # 如果已经是 .jpg，则跳过
        continue
    outputimg = os.path.join(outputpath, "%s.jpg" % (file_name))
    img.save(outputimg)
    print(str(num0) + " " + inputpath + name + "  ==>  " + outputpath + outputimg)
    num0 += 1
