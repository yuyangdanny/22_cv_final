import glob
import os
import shutil
'''# 把yolo_label貼到foggy dataset
data_path = './data/leftImg8bit_trainvaltest/leftImg8bit_foggy'
path = './new_labels'
dirlist = os.listdir(path)
for i in dirlist:
    if os.path.isdir(path + '/' + i):
        another_dir = os.listdir(path + '/' + i)
        for j in another_dir:
            if os.path.isdir(path + '/' + i + '/' + j):
                now_dir = os.listdir(path + '/' + i + '/' + j)
                for file_name in now_dir:
                    only_name = file_name.split('.')
                    # print(path + '/' + i + '/' + j + '/' + file_name, data_path + '/' + i + '/' + j + '/' + only_name[0] + '_foggy_beta_0.01.txt')
                    shutil.copy(path + '/' + i + '/' + j + '/' + file_name, data_path + '/' + i + '/' + j + '/' + only_name[0] + '_foggy_beta_0.01.txt')
                    shutil.copy(path + '/' + i + '/' + j + '/' + file_name, data_path + '/' + i + '/' + j + '/' + only_name[0] + '_foggy_beta_0.02.txt')
                    shutil.copy(path + '/' + i + '/' + j + '/' + file_name, data_path + '/' + i + '/' + j + '/' + only_name[0] + '_foggy_beta_0.005.txt')
                print('Done copy: ' + data_path + '/' + i + '/' + j)
                    
                    # print(path + '/' + i + '/' + j + '/' + file_name)
'''
'''# 把yolo_label貼到non foggy dataset
data_path = './data/leftImg8bit_trainvaltest/leftImg8bit'
path = './new_labels'
dirlist = os.listdir(path)
for i in dirlist:
    if os.path.isdir(path + '/' + i):
        another_dir = os.listdir(path + '/' + i)
        for j in another_dir:
            if os.path.isdir(path + '/' + i + '/' + j):
                now_dir = os.listdir(path + '/' + i + '/' + j)
                for file_name in now_dir:
                    # print(data_path + '/' + i + '/' + j)
                    shutil.copy(path + '/' + i + '/' + j + '/' + file_name, data_path + '/' + i + '/' + j)
'''