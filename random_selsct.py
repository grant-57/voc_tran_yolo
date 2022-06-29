# -*- coding: utf-8 -*-
"""
将数据集划分为训练集，验证集，测试集
"""

import os
import random
import shutil
# 创建保存图像的文件夹
def makedir(new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)


def moveFile(dataset_dir, train_dir, valid_dir, test_dir, train_pct, valid_pct, test_pct):
    pathDir = os.listdir(dataset_dir)  # 取图片的原始路径
    filenumber = len(pathDir)
    rate1 = train_pct  # 自定义抽取csv文件的比例，比方说100张抽80张，那就是0.8
    picknumber1 = int(filenumber * rate1)  # 按照rate比例从文件夹中取一定数量的文件
    sample1 = random.sample(pathDir, picknumber1)  # 随机选取picknumber数量的样本
    for name in sample1:
        shutil.move(dataset_dir + name, train_dir + "//" + name)

    pathDir = os.listdir(dataset_dir)  # 取图片的原始路径
    filenumber = len(pathDir)
    rate2=valid_pct / (valid_pct+test_pct) #选验证集
    picknumber2 = int(filenumber * rate2)  # 按照rate比例从文件夹中取一定数量的文件
    sample2 = random.sample(pathDir, picknumber2)  # 随机选取picknumber数量的样本
    for name in sample2:
        shutil.move(dataset_dir + name, valid_dir + "//" + name)

    pathDir = os.listdir(dataset_dir)  # 取图片的原始路径
    filenumber = len(pathDir)
    rate3=1 #选测试集
    picknumber3 = int(filenumber * rate3)  # 按照rate比例从文件夹中取一定数量的文件
    sample3 = random.sample(pathDir, picknumber3)  # 随机选取picknumber数量的样本
    for name in sample3:
        shutil.move(dataset_dir + name, test_dir + "//" + name)
    return


def random_select(dataset_dir, train_dir, valid_dir, test_dir, train_pct, valid_pct, test_pct):
    makedir(train_dir)
    makedir(valid_dir)
    makedir(test_dir)
    moveFile(dataset_dir, train_dir, valid_dir, test_dir, train_pct, valid_pct, test_pct)
    return


