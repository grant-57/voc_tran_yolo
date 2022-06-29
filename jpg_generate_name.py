import os
import random

def makedir(new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
def jpg_name(train_dir, valid_dir, test_dir, name_dir):
    makedir(name_dir)
    train_namesavepath = './name//train_name.txt'
    total_xml = os.listdir(train_dir)
    num = len(total_xml)
    list = range(num)
    ftrain = open(train_namesavepath, 'w')
    for i in list:
        name = total_xml[i][:-4] + '\n'
        ftrain.write(name)
    ftrain.close()

    valid_namesavepath = './name//valid_name.txt'
    total_xml = os.listdir(valid_dir)
    num = len(total_xml)
    list = range(num)
    fvalid = open(valid_namesavepath, 'w')
    for i in list:
        name = total_xml[i][:-4] + '\n'
        fvalid.write(name)
    fvalid.close()

    test_namesavepath = './name//test_name.txt'
    total_xml = os.listdir(test_dir)
    num = len(total_xml)
    list = range(num)
    ftest = open(test_namesavepath, 'w')
    for i in list:
        name = total_xml[i][:-4] + '\n'
        ftest.write(name)
    ftest.close()
    return train_namesavepath, valid_namesavepath, test_namesavepath