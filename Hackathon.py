from utils.utils import *

# # 1. 创建XML文件并写入
# image_path = "dataset\\VOC2007\\images\\"
# old_label_path = "dataset\\VOC2007\\labels_xml\\"
# try:
#     shutil.rmtree(new_label_path)
# except:
#     pass
# mkdir(new_label_path)
# for name in read_fileName_in_path(old_label_path):
#     newbndbox = Category_mapping_with_Hackathon3(read_xml_annotation(old_label_path, name))
#     crate_xml_file(new_label_path, name, image_path, newbndbox)
# print("xml file crate finish")

# # 2. 数据增量
# AUGPath = "dataset\\AUG_DIR\\"
# source_img_path = "dataset\\VOC2012\\JPEGImages\\"
# source_xml_path = "dataset\\Source_Path\\labels_xml\\"
# file_Prefix = "AUG_PATH"
# seq = iaa.Sequential([
#     # iaa.Flipud(0.5),  # 垂直翻转所有图像的20％
#     # iaa.Fliplr(0.5),  # 镜像
#     iaa.Multiply((1.2, 1.5)),  # 改变亮度，不影响BBs
#     iaa.GaussianBlur(sigma=(0, 1.0)),  # 高斯模糊
#     iaa.Affine(
#         translate_px={"x": 15, "y": 15},
#         scale=(0.8, 0.95),
#         rotate=(-30, 30)
#     )  # 在x/y轴上平移40/60px，缩放到50-70％，影响BBs
# ])
# label_file_list = find_label_in_path(source_xml_path,'pedestrian')
# data_enhancement(seq,2,AUGPath,source_img_path,source_xml_path,label_file_list,file_Prefix,1)


# # 3. 统计标签分类
# new_label_path = "automatic_labeling/auto_labelimg/dataset/output_VOC_dir"
# label_list = []
# for filename in read_fileName_in_path(new_label_path):
#     for name in num_of_xmllabels_read(new_label_path, filename):
#         label_list.append(name)
# final_list = pd.value_counts(label_list)
# # print(list(set(label_list)))
# # print(list(set(final_list)))
# # print(final_list["dog"])
# print(final_list)

# # 4. 删除多余文件
labelPath = "Dataset/final_dataset/labels/"
imagePath = "Dataset/final_dataset/images/"
removefile(labelPath, imagePath)
removefile(imagePath, labelPath)

# # 5. 添加文件前缀
# finalImagePath = "dataset\\VOC2007\\images\\"
# finalLabelPath = "dataset\\VOC2007\\labels_xml\\"
# add_fileprefox(finalLabelPath,"VOC2007_trainval_")
# add_fileprefox(finalImagePath,"VOC2007_trainval_")

# 6. 从两个目录内分组复制文件
# source_path_1 = "dataset\\CCTSDB\\images\\"
# source_path_2 = "dataset\\CCTSDB\\New_labels_xml\\"
# copy_few = 3
# write_path = "few_path\\"
# copy_file_in_two_path(source_path_1,source_path_2,copy_few,write_path)

# # 7. kitti to VOC xmlfile
# kitti_file_path = "Dataset/dataset/data/labels/"
# output_path = "Dataset/dataset/data/xml/"
# img_path = "Dataset/dataset/data/img"
# kitti_to_VOCxml(kitti_file_path,output_path,img_path)
# kitti_to_VOCxml(kitti_file_path,output_path)

# # 9. 替换所有标签到指定标签
# source_path = "dataset\\CCTSDB\\labels_xml\\"
# label_name = "road_sign"
# write_path = "dataset\\CCTSDB\\New_labels_xml\\"
# # write_path = None
# change_all_label_name(source_path,label_name,write_path)

# 10. 将标签处理成YOLO训练需要用的
## 旧有方法 已舍弃 ##
# Absolute_path = "C:/Hackathon"
# xml_path = "training/labels_xml/"
# img_path = "training/images/"
# label_list = ['vehicle', 'bicycle', 'pedestrian', 'road_sign']
# take_dataset_to_YOLOtrain(Absolute_path,xml_path,img_path,label_list)

# 11. 过滤过小的标签
# old_xml_path = "training/mosica_labels_xml/"
# img_path = "training/mosica_images/"
# new_xml_path = "training/mosica_labels_xml_changed/"
# mkdir(new_xml_path)
# zero = 0
# for filename in read_fileName_in_path(old_xml_path):
#     oldbndbox = read_xml_annotation(old_xml_path,filename)
#     newbndbox,index = filter_the_labels(oldbndbox,10)
#     crate_xml_file(new_xml_path,filename,newbndbox,"mosaic_filter_file",img_path)
#     zero += index
# print(zero)

# # 12. 过滤过暗或过暗的图片
# img_path = "bicycle_dataset/tdcb_leftImg8bit_train/leftImg8bit/train/tsinghuaDaimlerDataset/"
# output_path = "bicycle_dataset/tdcb_leftImg8bit_train/leftImg8bit/train/changed_images_da-1/"
# move_bright_or_dark_img_to_new_folder(img_path,output_path)

# # 13. 移动文件
# from_path = "automatic_labeling/auto_labelimg/dataset/img/"
# to_path = "automatic_labeling/auto_labelimg/dataset/few_5/A/images/"
# os.mkdir(to_path)
# file_name_list = read_fileName_in_path("automatic_labeling/auto_labelimg/dataset/few_5/A/labels/")

# # 14. 变更指定标签到对应标签
# source_path = "Hackathon_3_tool_code/few_path/few_path_3/labels_xml/"
# source_label = "pedestrain"
# specified_label = "pedestrian"
# write_path = "Hackathon_3_tool_code/few_path/few_path_3/New_labels_xml/"
# change_specified_label_name(source_path,source_label,specified_label,write_path)

# # 15. Hackathon val label to VOC
# label_path = "val_training/labels/"
# output_path = "val_training/label_xml/"
#
# for file_name in read_fileName_in_path(label_path):
#     bndbox = get_box_from_val_path(label_path,file_name)
#     crate_xml_file(output_path,file_name,bndbox)

# # 16. VOC to kitti
# xml_path = "Dataset/animal_dataset/xml/"
# write_path = "Dataset/animal_dataset/labels/"
# VOC_to_kitti(xml_path, write_path)

# # 17. 删除带有指定类别的标签
# spec_word = "monkey"
# file_dir = "Dataset/Monkey_Cat_and_Dog_detection/dataset/xml"
# remove_file_list = []
# file_name_list = read_fileName_in_path(file_dir)
# for filename in file_name_list:
#     bndboxlist = read_xml_annotation(file_dir,filename)
#     for bndbox in bndboxlist:
#         if spec_word == str(bndbox[0]):
#             remove_file_list.append(filename)
# print("there are " + str(len(list(set(remove_file_list)))) + " files will be removed")
# for file_name in list(set(remove_file_list)):
#     os.remove(file_dir + "/" + file_name)

# removefile("Dataset/Monkey_Cat_and_Dog_detection/dataset/xml/",
#            "Dataset/Monkey_Cat_and_Dog_detection/dataset/img/")

# 18. 创建新的xml文件，从旧文件中筛选出有效标签
# xml_file_dir = "Dataset/animal_dataset/xml/"
# img_file_dir = "Dataset/animal_dataset/img/"
# output_xml_file_dir = "Dataset/animal_dataset/output_xml/"
# allow_sort = ["cat","dog","horse"]
#
# xml_file_name_list = read_fileName_in_path(xml_file_dir)
# for file_name in xml_file_name_list:
#     new_bndbox = []
#     bndboxs = read_xml_annotation(xml_file_dir,file_name)
#     for bndbox in bndboxs:
#         if bndbox[0] in allow_sort:
#             new_bndbox.append(bndbox)
#     print(new_bndbox)
#     crate_xml_file(output_xml_file_dir,file_name,new_bndbox,"Hackathon5",img_file_dir)

# 19.jpg2png
# input_imgdir = "automatic_labeling/auto_labelimg/dataset/img_jpeg/"
# output_imgdir = "automatic_labeling/auto_labelimg/dataset/img/"
# file_name_list = read_fileName_in_path(input_imgdir)
# for filename in file_name_list:
#     img = Image.open(input_imgdir + filename,"r")
#     img.save(output_imgdir + filename.split(".")[0] + ".png")

# 20. yolo2voc
# yolo_labeldir = "automatic_labeling/auto_labelimg/runs/detect/exp/labels/"
# img_dir = "automatic_labeling/auto_labelimg/dataset/img/"
# output_dir = "automatic_labeling/auto_labelimg/runs/output_VOC_dir_2/"
# class_list = ["cat","dog","horse"]
# for file_name in read_fileName_in_path(yolo_labeldir):
#     yolo2voc(yolo_labeldir,output_dir,file_name,img_dir,class_list)

# # 21. 创建nemo数据集
# # 构建对照字典
# contrast_dict = {
#     "cat": "请指出哪个图片的序列号是1",
#     "dog": "请指出哪个图片的序列号是2",
#     "horse": "请指出哪个图片的序列号是3",
#     "person": "请指出哪个图片的序列号是4"}
# # 取出wav文件列表
# wav_dir = "./test_floder/asr_wavdata/"
# # 语音数据集输出文件夹
# output_dir = "./wav_dataset/"
# # 测试集和验证机拆分比例系数
# scale_factor = 0.9
# creat_nemo_datset(contrast_dict,wav_dir,output_dir,scale_factor)

# # 22. PNG2IMG
# from pathlib import Path
# from PIL import Image
#
# inputPath = Path("Dataset/final_dataset/images")
# inputFiles = inputPath.glob("**/*.png")
# outputPath = Path("Dataset/final_dataset/images")
# for f in inputFiles:
#     outputFile = outputPath / Path(f.stem + ".jpg")
#     im = Image.open(f)
#     im.save(outputFile)
