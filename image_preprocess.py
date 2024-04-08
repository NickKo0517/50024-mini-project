import cv2 as cv
import PIL.Image as Image
import numpy as np
from collections import Counter
from pathlib import Path
import matplotlib.pyplot as plt         # to display image

train_small_path = 'D:\\Download\\train'
output_path = "D:\\Download\\train_processed"

# load all image file names into this script
base_dir = Path(train_small_path)
raw_names = [entry.name for entry in base_dir.iterdir() if entry.is_file()]
image_names = [train_small_path + "\\" + name for name in raw_names]
out_file_paths = [0] * len(image_names)

print(image_names[0])
print(raw_names[0])

""" convert all images to grey scale and crop faces """
gray: str = 'gray_'

# load classifier(s)
face_cascade1 = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
# process every single image
img_skipped = 0
writer = open('valid_img_names.csv', 'w')
writer.write('File Name\n')
for i,(path,raw_name) in enumerate(zip(image_names, raw_names)):
    # load image in: first read with PIL
    img = cv.imread(path, cv.IMREAD_GRAYSCALE)
    if img is None: #first check if it can be opened
        img_skipped += 1
        continue
    # Detect faces (returns a rectangle/matrix which contains the face)
    #face contains (starting) coordinates and width/height of face detected
    face1 = face_cascade1.detectMultiScale(img, scaleFactor=1.1, minNeighbors=12) 
    # crop out face 
    if len(face1) < 1:
        # if no face detected, skip this image
        img_skipped += 1
        continue
    x,y,w,h = face1[0]
    cropped_face = img[y:y+h, x:x+w]
    # save to directory
    filename = output_path+'\\'+gray+raw_name
    out_file_paths[i] = filename
    print(filename)
    cv.imwrite(filename=filename, img=cropped_face)
    writer.write("{}\n".format(raw_name))
writer.close()
print('skipped {} images.'.format(img_skipped))
print('processed {} images'.format(len(out_file_paths) - out_file_paths.count(0)))


# cv.waitKey(delay=0)   #delay=0 means showing forever until manually close the image