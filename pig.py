import cv2
import os
import glob2
import numpy as np

IMG_PATH = '..\data\dataset\pig-train\\000000001.jpg'
LABEL_PATH = '../data/dataset/pig-train/000000001.txt'
PATH = "..\data\dataset\pig-train\\"
def readLabel(path):
    with open(path) as file:
        listLabel = []
        listLabel = file.readlines()

    return listLabel

def readLabelPath(nameLabel):
    name = nameLabel + ".txt"
    all_files = []
    for ext in [name]:
        images = glob2.glob(os.path.join(PATH, ext))
        all_files += images
    return all_files[0]

def readImagePath():
    all_files = []
    for ext in ["*.jpg"]:
        images = glob2.glob(os.path.join(PATH, ext))
        all_files += images
    return all_files

def splitImagePath(imagePath):
    arr = imagePath.split("\\")
    name = arr[-1]
    name = name.split(".")
    name = name[0]
    return name

def splitLabel(label):
    arr = label.split(" ")
    cx, cy, w, h  = float(arr[1]), float(arr[2]), float(arr[3]), float(arr[4])
    return cx, cy, w, h

def cropImage():
    files = readImagePath()
    for imgPath in files:
        img = cv2.imread(imgPath)
        width, height = img.shape[0], img.shape[1]

        name = splitImagePath(imgPath)
        labelPath = readLabelPath(name)
        listLabel = readLabel(labelPath)

        count = 0
        for label in listLabel:
            print(name)
            cx, cy, w, h = splitLabel(label)
            x1 = (int)(((w+2*cx)*width)/2)
            x2 = (int)(((3*w+2*cx)*width)/2)

            y1 = (int)(((h+2*cy)*height)/2)
            y2 = (int)(((3*h+2*cy)*height)/2)

            # x1 = min(x1,x2)
            # x2 = max(x1,x2)
            # y1 = min(y1,y2)
            # y2 = max(y1,y2)
            # cx = (int)(cx)
            # cy = (int)(cy)
            # w = (int)(w)
            # h = (int)(h)

            img_crop = img[x1:x2, y1:y2, :]

            #count = 0
            file_name = "./labelimg" + name + str(count)+".jpg"
            print(file_name)
            # file_name = os.path.join("labeling", tmp)
            count += 1
            cv2.imwrite(file_name, img_crop)

        break

if __name__ == "__main__":
    cropImage()
    



