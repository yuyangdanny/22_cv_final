from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
import numpy as np
img = Image.open('./data/aachen_000000_000019_leftImg8bit_foggy_beta_0.01.png')
''' Gaussian Blur
# 模糊半径越大, 正态分布标准差越大, 图像就越模糊 (kernel_size, sigma)
# transform_1 = transforms.GaussianBlur(21, 10)
# img_1 = transform_1(img)
transform_2 = transforms.GaussianBlur(101, 10)
img_2 = transform_2(img)
# transform_3 = transforms.GaussianBlur(101, 100)
# img_3 = transform_3(img)
img_2.save('./data/aachen_000000_000019_leftImg8bit_foggy_beta_0.01_gaussian_blur.png')
'''
'''
class SaltAndPepperNoise(object):
    r""" Implements 'Salt-and-Pepper' noise
    Adding grain (salt and pepper) noise
    (https://en.wikipedia.org/wiki/Salt-and-pepper_noise)

    assumptio
    n: high values = white, low values = black
    
    Inputs:
            - threshold (float):
            - imgType (str): {"cv2","PIL"}
            - lowerValue (int): value for "pepper"
            - upperValue (int): value for "salt"
            - noiseType (str): {"SnP", "RGB"}
    Output:
            - image ({np.ndarray, PIL.Image}): image with 
                                               noise added
    """
    def __init__(self,
                 treshold:float = 0.005,
                 imgType:str = "cv2",
                 lowerValue:int = 5,
                 upperValue:int = 250,
                 noiseType:str = "SnP"):
        self.treshold = treshold
        self.imgType = imgType
        self.lowerValue = lowerValue # 255 would be too high
        self.upperValue = upperValue # 0 would be too low
        if (noiseType != "RGB") and (noiseType != "SnP"):
            raise Exception("'noiseType' not of value {'SnP', 'RGB'}")
        else:
            self.noiseType = noiseType
        super(SaltAndPepperNoise).__init__()

    def __call__(self, img):
        if self.imgType == "PIL":
            img = np.array(img)
        if type(img) != np.ndarray:
            raise TypeError("Image is not of type 'np.ndarray'!")
        
        if self.noiseType == "SnP":
            random_matrix = np.random.rand(img.shape[0],img.shape[1])
            img[random_matrix>=(1-self.treshold)] = self.upperValue
            img[random_matrix<=self.treshold] = self.lowerValue
        elif self.noiseType == "RGB":
            random_matrix = np.random.random(img.shape)      
            img[random_matrix>=(1-self.treshold)] = self.upperValue
            img[random_matrix<=self.treshold] = self.lowerValue
        
        

        if self.imgType == "cv2":
            return img
        elif self.imgType == "PIL":
            # return as PIL image for torchvision transforms compliance
            return PIL.Image.fromarray(img)

SnP_noise = SaltAndPepperNoise()
array_img = np.asarray(img)
pepper_noise = SnP_noise(array_img.copy())
pepper_noise = Image.fromarray(pepper_noise)
pepper_noise.save('./data/aachen_000000_000019_leftImg8bit_foggy_beta_0.01_s&p.png')
'''
distortion_scale = 0.5
p = 1
fill = (0, 0, 0)
transform = transforms.RandomPerspective(distortion_scale=distortion_scale, p=p, fill=fill)
print(type(img))
random_perspective = transform(img)
random_perspective.save('./data/aachen_000000_000019_leftImg8bit_foggy_beta_0.01_geometric_distortion.png')
