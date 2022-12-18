import os
import random

path = '/media/NFS/wendy/yolov7/data/leftImg8bit_trainvaltest/leftImg8bit/val'
dirlist = os.listdir(path)
only_png_list = []
for i in dirlist:
    if os.path.isdir(path + '/' + i):
        another_dir = os.listdir(path + '/' + i)
        for x in range(len(another_dir)):
            txt_or_png = another_dir[x].split('.')[1]
            if txt_or_png == 'png':
                only_png_list.append(path + '/' + i + '/' + another_dir[x])
random.shuffle(only_png_list)
non_foggy_list = only_png_list[:round(len(only_png_list) * 0.7)]
foggy_list = only_png_list[round(len(only_png_list) * 0.7):]
# print(new_file_list)
real_foggy_list = []
for idx in range(len(foggy_list)):
    foggy_split = foggy_list[idx].split('leftImg8bit/')
    extension_split = foggy_split[1].split('.')
    real_foggy_list.append(foggy_split[0] + 'leftImg8bit_foggy/' + extension_split[0] + '_foggy_beta_0.01.png')
    # print(foggy_split[0] + 'leftImg8bit_foggy/' + extension_split[0] + '_foggy_beta_0.01.png')
    # print(foggy_split[1])
    # print(foggy_list[idx])
final_list = non_foggy_list + real_foggy_list
random.shuffle(final_list)
f= open("./data/val.txt","w+")
for i in range(len(final_list)):
    f.write(final_list[i] + "\n")
f.close()