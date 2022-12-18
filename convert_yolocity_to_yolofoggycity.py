import json
import os
from pathlib import Path
import re
from tqdm import tqdm
import shutil


def mkdir(url):
    if not os.path.exists(url):
        os.makedirs(url)


if __name__ == '__main__':
    
    # root_dir = Path(__file__).parent
    # image_dir = root_dir / 'leftImg8bit_foggy'
    # image_output_root_dir = root_dir / 'images'
    # label_output_root_dir = root_dir / 'labels'  # 来自cityscapes的yolo txt标注文件
    
    root_dir = '/media/public_dataset/CityScape-Foggy/'
    image_dir = root_dir + 'leftImg8bit_foggy_/leftImg8bit_foggy'
    label_dir = root_dir + 'gtFine_trainvaltest/gtFine'
    image_output_root_dir = './foggy_cityscape/images'
    label_output_root_dir = './labels'

    foggy_rates = [0.01, 0.02, 0.005]  # 根据实际情况调整

    for _t_ in tqdm(['train', 'test', 'val']):
        mkdir(image_output_root_dir + '/' + _t_)
        # 'berlin_000000_000019_leftImg8bit.png' -> 'berlin_000000_000019_leftImg8bit_foggy_beta_0.01.png'
        # 复制标签
        for cities_name in os.listdir(label_output_root_dir + '/' + _t_):
            for label_file in os.listdir(label_output_root_dir + '/' + _t_ + '/' + cities_name).copy():
                for fr in foggy_rates:
                    print(label_output_root_dir + '/' + _t_ + '/' + label_file + '/' + cities_name)
                    shutil.copy(label_output_root_dir + '/' + _t_ + '/' + label_file,
                                label_output_root_dir + '/' + _t_ + '/' + f'{Path(label_file).stem}_foggy_beta_{fr}.txt')
                os.remove(label_output_root_dir + '/' + _t_ + '/' + label_file)
        # 复制文件
        type_files = []
        for city_name in os.listdir(image_dir + '/' + _t_):
            for img_file in os.listdir(image_dir + '/' + _t_ + '/' + city_name):
                shutil.copy(image_dir + '/' + _t_ + '/' + city_name + '/' + img_file, image_output_root_dir + '/' + _t_ + '/' + img_file)  # 复制移动
                type_files.append(f'./images/{_t_}/{img_file}\n')

        with open(root_dir + '/' + f"yolo_{_t_}.txt", 'w') as f:  # 记录训练样本等的具体内容
            f.writelines(type_files)
# https://blog.csdn.net/Shenpibaipao/article/details/111257995