import keras
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
from pathlib import Path
import time     #timing


train_path = 'D:\\Download\\train\\'
output_path = "D:\\Download\\train_processed"
outfile_name = r"D:\Download\train_features"
# load all image file names into this script
base_dir = Path(train_path)

model = ResNet50(weights='imagenet')

"""Code For Debugging"""
# img = keras.utils.load_img(train_path + '0.jpg', target_size=(210, 210))
# x = keras.utils.img_to_array(img)
# x = np.expand_dims(x, axis=0)
# x = preprocess_input(x)
# print(x.shape)

matrixArray = [0] * 69_540
# for i,file in enumerate(base_dir.iterdir()):
#     if file.is_file():
#         img_path = train_path + file.name
#         img = keras.utils.load_img(img_path, target_size=(210, 210))
#         x = keras.utils.img_to_array(img)
#         x = np.expand_dims(x, axis=0)
#         x = preprocess_input(x)
#         matrixArray[i] = x

# for i in range(2):
#     img_path = train_path + f"{i}.jpg"
#     img = keras.utils.load_img(img_path, target_size=(210, 210))
#     x = keras.utils.img_to_array(img)
#     x = np.expand_dims(x, axis=0)
#     x = preprocess_input(x)
#     matrixArray[i] = x
print(f'extracted {sum(matrixArray[matrixArray != 0])} from {len(matrixArray)} images')






