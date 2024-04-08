import cv2 as cv
import PIL.Image as Image
import numpy as np
from collections import Counter
from pathlib import Path


def resize_img(raw_img: np.ndarray, w_std: int, h_std: int)->np.ndarray:
    resized = np.zeros((w_std, h_std))
    w,h = raw_img.shape
    if w < w_std or h < h_std:  # needs upsizing
        resized = cv.resize(raw_img, dsize=resized.shape, interpolation=cv.INTER_AREA)
    else:   #shrink size
        resized = cv.resize(raw_img, dsize=resized.shape, interpolation=cv.INTER_LINEAR)
    return resized

def find_most_common_shape(dim_list: list[list[int,int]])->tuple[int,int]:
    return Counter(dim_list).most_common(1)[0][0]


if __name__ == '__main__':
    grey_img_dir = r"D:\Download\train_processed"
    resized_dir = grey_img_dir

    # load all image path names to code
    base_dir = Path(grey_img_dir)
    raw_names = [entry.name for entry in base_dir.iterdir() if entry.is_file()]
    image_names = [grey_img_dir + "\\" + name for name in raw_names]

    # find most common shape
    # shape_list = [np.asarray(Image.open(path).convert('L')).shape 
    #               for path in image_names]
    # print(shape_list[:3])
    # shape_matrix = np.array(shape_list)
    # print(shape_matrix[:3,:])

    # commonDim, maxDim, medDim, meanDim, minDim = find_most_common_shape(shape_list), max(shape_list), \
    # np.median(shape_matrix, axis=0), np.mean(shape_matrix, axis=0), min(shape_list)
    # print(f'commonDim = {commonDim}')
    # print(f'max dimension = {maxDim}')
    # print(f'median dimension = {medDim}')
    # print(f'mean dimension = {meanDim}')
    # print(f'mode dimension (commonDim) = {commonDim}')
    # print(f'min dimension = {minDim}')

    # resize all image's dimension to median of all of them
    w_std, h_std = 210,210
    img_processed: int = 0
    for path in image_names:
        raw_img = Image.open(path).convert('L')
        resized = np.asarray(raw_img.resize((w_std, h_std)))
        if resize_img is not None:
            img_processed += 1
        print('resize ' + path)
        cv.imwrite(path, resized)
    print(f'processed {img_processed} images')

    num_img: int = 0
    for img in base_dir.iterdir():
        if img.is_file():
            num_img += 1
    print(f"total {num_img} images")