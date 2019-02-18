import cv2
import os, os.path
import numpy as np

inputDir = input("enter input directory > ")
inputDir = inputDir + "\\"


image_path_list = []
valid_image_extensions = [".JPG", ".jpeg", ".png", ".tif", ".tiff"]
valid_image_extensions = [item.lower() for item in valid_image_extensions]

for file in os.listdir(inputDir):
    ##print (file)
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(file)
##print (image_path_list)
gamma = 0.1

def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
       for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

cpt=0
os.chdir(inputDir)
if not os.path.isdir(inputDir + 'output'):
    os.mkdir('output')

outputDir = os.path.join(inputDir,"output\\")
for imageFile in image_path_list:
    imagePath = inputDir + imageFile
    image = cv2.imread(imagePath)
    cv2.imshow(imagePath, image)
    adjusted = adjust_gamma(image, gamma=gamma)
    imageOutputPath = outputDir + imageFile 
    cv2.imwrite(imageOutputPath, adjusted)
    cpt += 1
    key = cv2.waitKey(0)
    if key == 27: # escape
        break
    
cv2.destroyAllWindows()