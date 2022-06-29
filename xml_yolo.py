# -*- coding: utf-8 -*-
"""
将数据集划分为训练集，验证集，测试集
"""

import os
import random
import shutil
from random_selsct import random_select
from jpg_generate_name import jpg_name
from select_txt import select_txt

# 1.确定原图像数据集路径
dataset_dir = "./JPEGImages/"  ##所有图片路径
labels_dir = "./label/"  ##所有yolo标签的路径
# 2.确定数据集划分后保存的路径
# split_dir = "D:/test2021/after0811/"  ##划分后保存路径
train_dir = "./images//train"
valid_dir = "./images//val"
test_dir = "./images//test"
labels_train_dir = "./labels//train"
labels_valid_dir = "./labels//val"
labels_test_dir = "./labels//test"
name_dir = "./name"
# 3.确定将数据集划分为训练集，验证集，测试集的比例
train_pct = 0.8
valid_pct = 0.1
test_pct = 0.1
# 4.划分
random_select(dataset_dir, train_dir, valid_dir, test_dir, train_pct, valid_pct, test_pct)
# 5.写名单
train_namesavepath, valid_namesavepath, test_namesavepath = jpg_name(train_dir, valid_dir, test_dir, name_dir)
# 6.写labels
select_txt(labels_dir,labels_train_dir,labels_valid_dir,labels_test_dir,train_namesavepath,valid_namesavepath,test_namesavepath)





