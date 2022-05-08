import codecs
import json

import librosa

from utils.utils import *

'''
# 首先构建这样一个对照字典
contrast_dict = {"文件名关键词": "语音内容"}

# 输出的数据集结构
wav_dataset
  ├─ train
  │   ├─ xxx.wav
  │   └─ xxx.wav
  ├─ val
  │   ├─ xxx.wav
  │   └─ xxx.wav
  ├─ train.json
  └─ val.json
'''
# 创建nemo数据集

# 构建对照字典
contrast_dict = {
    "asr_cat": "请指出哪个图片的序列号是1",
    "asr_dog": "请指出哪个图片的序列号是2",
    "asr_horse": "请指出哪个图片的序列号是3",
    "asr_person": "请指出哪个图片的序列号是4",
    "cat": "请指出哪个图片的序列号是1",
    "dog": "请指出哪个图片的序列号是2",
    "horse": "请指出哪个图片的序列号是3",
    "person": "请指出哪个图片的序列号是4"}

# 取出wav文件列表
wav_dir = "test_floder/asr_wavdata/"
# 语音数据集输出文件夹
output_dir = "./wav_dataset/"
# 测试集和验证机拆分比例系数
scale_factor = 0.9
mkdir(output_dir + "train/")
mkdir(output_dir + "val/")

# 输入的音频文件名列表
wav_list = read_fileName_in_path(wav_dir)
# 指定json文件
train_json = codecs.open(output_dir + "train.json", "w", "utf-8")
val_json = codecs.open(output_dir + "val.json", "w", "utf-8")

# 创建文件名对应标签类型字典
label_dict = {}
for key in list(contrast_dict.keys()):
    label_dict[key] = {"filenamelist": [], "train_num": 0, "val_num": 0}
for filename in wav_list:
    for key in list(contrast_dict.keys()):
        if key in filename:
            label_dict[key]["filenamelist"].append(filename)
    for key in list(contrast_dict.keys()):
        label_dict[key]["train_num"] = int(len(label_dict[key]["filenamelist"]) * scale_factor)
print(label_dict)

# 根据标签字典复制文件到数据集
for key in label_dict.items():
    num = 1
    if key[1]["filenamelist"] != []:
        for filename in key[1]["filenamelist"]:
            json_basic_dict = {}
            if num <= key[1]["train_num"]:
                shutil.copy(wav_dir + filename, output_dir + "train/")
                json_basic_dict["audio_filepath"] = output_dir + "train/" + filename
                json_basic_dict["duration"] = librosa.get_duration(filename=wav_dir + filename)
                json_basic_dict["text"] = contrast_dict[key[0]]
                json.dump(json_basic_dict, train_json, ensure_ascii=False)
                train_json.write("\n")
            else:
                shutil.copy(wav_dir + filename, output_dir + "val/")
                json_basic_dict["audio_filepath"] = output_dir + "val/" + filename
                json_basic_dict["duration"] = librosa.get_duration(filename=wav_dir + filename)
                json_basic_dict["text"] = contrast_dict[key[0]]
                json.dump(json_basic_dict, val_json, ensure_ascii=False)
                val_json.write("\n")
            num += 1
train_json.close()
val_json.close()
